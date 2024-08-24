import * as vscode from "vscode";
import * as path from "path";
import * as fs from "fs";

export class PreviewProvider implements vscode.TextDocumentContentProvider {
  public static readonly viewType = "instruct.preview"; // Define viewType as public static
  private readonly _onDidChange = new vscode.EventEmitter<vscode.Uri>();
  readonly onDidChange = this._onDidChange.event;

  provideTextDocumentContent(uri: vscode.Uri): string | Thenable<string> {
    const filePath = uri.path.slice(1); // Remove leading '/'
    return new Promise((resolve, reject) => {
      fs.readFile(filePath, "utf8", (err, data) => {
        if (err) {
          reject(err);
          return;
        }
        resolve(data);
      });
    });
  }

  update(uri: vscode.Uri) {
    this._onDidChange.fire(uri);
  }
}

export function activate(context: vscode.ExtensionContext) {
  const previewProvider = new PreviewProvider();
  context.subscriptions.push(
    vscode.workspace.registerTextDocumentContentProvider(
      PreviewProvider.viewType,
      previewProvider
    )
  );

  vscode.languages.registerCodeActionsProvider("instruct", {
    provideCodeActions(
      document: vscode.TextDocument,
      range: vscode.Range
    ): vscode.CodeAction[] {
      const text = document.getText(range);
      const importMatch = text.match(/@import\s+(.+)$/);

      if (importMatch) {
        const importPath = importMatch[1];
        const action = new vscode.CodeAction(
          "Preview Import",
          vscode.CodeActionKind.QuickFix
        );
        action.command = {
          title: "Preview Import",
          command: "instruct.preview",
          arguments: [importPath],
        };
        return [action];
      }
      return [];
    },
  });

  context.subscriptions.push(
    vscode.commands.registerCommand(
      "instruct.preview",
      (importPath: string) => {
        const fileUri = vscode.Uri.file(
          path.resolve(vscode.workspace.rootPath || "", importPath)
        );
        vscode.commands
          .executeCommand(
            "vscode.previewHtml",
            fileUri,
            vscode.ViewColumn.Two,
            "Preview"
          )
          .then(
            (success) => {},
            (error) => {
              vscode.window.showErrorMessage(
                "Error opening preview: " + error.message
              );
            }
          );
      }
    )
  );
}
