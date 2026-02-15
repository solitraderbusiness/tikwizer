import { ContextMenu } from './ContextMenu';
import { ContextMenuItem } from './ContextMenuItem';
import { useEditorStore } from '../../../stores/editorStore';

interface CanvasContextMenuProps {
  x: number;
  y: number;
  flowPosition: { x: number; y: number };
  onClose: () => void;
}

export function CanvasContextMenu({ x, y, flowPosition, onClose }: CanvasContextMenuProps) {
  const clipboard = useEditorStore((s) => s.clipboard);
  const pasteNodes = useEditorStore((s) => s.pasteNodes);

  const handlePaste = () => {
    pasteNodes(flowPosition);
    onClose();
  };

  return (
    <ContextMenu x={x} y={y} onClose={onClose}>
      <ContextMenuItem
        label="Paste"
        shortcut="Ctrl+V"
        onClick={handlePaste}
        disabled={!clipboard || clipboard.nodes.length === 0}
      />
    </ContextMenu>
  );
}
