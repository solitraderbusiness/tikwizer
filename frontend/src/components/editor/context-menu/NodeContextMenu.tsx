import { ContextMenu } from './ContextMenu';
import { ContextMenuItem } from './ContextMenuItem';
import { ContextMenuDivider } from './ContextMenuDivider';
import { useEditorStore } from '../../../stores/editorStore';
import type { FlowNodeData } from '../../../types';

interface NodeContextMenuProps {
  nodeId: string;
  x: number;
  y: number;
  onClose: () => void;
  onRename: (nodeId: string) => void;
  onShowInfo: (nodeId: string) => void;
}

export function NodeContextMenu({ nodeId, x, y, onClose, onRename, onShowInfo }: NodeContextMenuProps) {
  const getSelectedNodeIds = useEditorStore((s) => s.getSelectedNodeIds);
  const duplicateNode = useEditorStore((s) => s.duplicateNode);
  const duplicateNodes = useEditorStore((s) => s.duplicateNodes);
  const removeNode = useEditorStore((s) => s.removeNode);
  const removeSelectedNodes = useEditorStore((s) => s.removeSelectedNodes);
  const detachNode = useEditorStore((s) => s.detachNode);
  const copyNodes = useEditorStore((s) => s.copyNodes);
  const cutNodes = useEditorStore((s) => s.cutNodes);
  const updateNodeData = useEditorStore((s) => s.updateNodeData);
  const createGroup = useEditorStore((s) => s.createGroup);
  const nodes = useEditorStore((s) => s.nodes);

  const selectedIds = getSelectedNodeIds();
  const isMultiSelect = selectedIds.length > 1 && selectedIds.includes(nodeId);
  const targetIds = isMultiSelect ? selectedIds : [nodeId];
  const node = nodes().find((n) => n.id === nodeId);
  const nodeData = node?.data as FlowNodeData | undefined;
  const isEnabled = nodeData?.enabled ?? true;

  const handleCopy = () => {
    copyNodes(targetIds);
    onClose();
  };

  const handleCut = () => {
    cutNodes(targetIds);
    onClose();
  };

  const handleDuplicate = () => {
    if (isMultiSelect) {
      duplicateNodes(targetIds);
    } else {
      duplicateNode(nodeId);
    }
    onClose();
  };

  const handleToggleEnabled = () => {
    for (const id of targetIds) {
      updateNodeData(id, { enabled: !isEnabled });
    }
    onClose();
  };

  const handleDetach = () => {
    for (const id of targetIds) {
      detachNode(id);
    }
    onClose();
  };

  const handleDelete = () => {
    if (isMultiSelect) {
      removeSelectedNodes();
    } else {
      removeNode(nodeId);
    }
    onClose();
  };

  const handleRename = () => {
    onRename(nodeId);
    onClose();
  };

  const handleInfo = () => {
    onShowInfo(nodeId);
    onClose();
  };

  const handleCreateGroup = () => {
    createGroup(targetIds);
    onClose();
  };

  return (
    <ContextMenu x={x} y={y} onClose={onClose}>
      <ContextMenuItem label="Edit Title" onClick={handleRename} />
      <ContextMenuDivider />
      <ContextMenuItem label="Copy" shortcut="Ctrl+C" onClick={handleCopy} />
      <ContextMenuItem label="Cut" shortcut="Ctrl+X" onClick={handleCut} />
      <ContextMenuItem label="Duplicate" shortcut="Ctrl+D" onClick={handleDuplicate} />
      <ContextMenuDivider />
      <ContextMenuItem
        label={isEnabled ? 'Disable' : 'Enable'}
        onClick={handleToggleEnabled}
      />
      <ContextMenuItem label="Detach from Flow" onClick={handleDetach} />
      <ContextMenuItem label="Information" onClick={handleInfo} />
      {isMultiSelect && (
        <>
          <ContextMenuDivider />
          <ContextMenuItem label="Create Area" onClick={handleCreateGroup} />
        </>
      )}
      <ContextMenuDivider />
      <ContextMenuItem label="Delete" shortcut="Del" onClick={handleDelete} danger />
    </ContextMenu>
  );
}
