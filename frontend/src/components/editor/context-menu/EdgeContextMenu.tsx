import { ContextMenu } from './ContextMenu';
import { ContextMenuItem } from './ContextMenuItem';
import { useEditorStore } from '../../../stores/editorStore';

interface EdgeContextMenuProps {
  edgeId: string;
  x: number;
  y: number;
  onClose: () => void;
}

export function EdgeContextMenu({ edgeId, x, y, onClose }: EdgeContextMenuProps) {
  const removeEdge = useEditorStore((s) => s.removeEdge);

  const handleDelete = () => {
    removeEdge(edgeId);
    onClose();
  };

  return (
    <ContextMenu x={x} y={y} onClose={onClose}>
      <ContextMenuItem label="Delete Connection" shortcut="Del" onClick={handleDelete} danger />
    </ContextMenu>
  );
}
