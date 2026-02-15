import { useEffect, useRef, useState } from 'react';
import { createPortal } from 'react-dom';
import { useEditorStore } from '../../../stores/editorStore';
import type { FlowNodeData } from '../../../types';

interface InlineRenameInputProps {
  nodeId: string;
  x: number;
  y: number;
  onClose: () => void;
}

export function InlineRenameInput({ nodeId, x, y, onClose }: InlineRenameInputProps) {
  const nodes = useEditorStore((s) => s.nodes);
  const updateNodeData = useEditorStore((s) => s.updateNodeData);
  const node = nodes().find((n) => n.id === nodeId);
  const nodeData = node?.data as FlowNodeData | undefined;
  const [value, setValue] = useState(nodeData?.blockName ?? '');
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    const el = inputRef.current;
    if (el) {
      el.focus();
      el.select();
    }
  }, []);

  const save = () => {
    const trimmed = value.trim();
    if (trimmed && trimmed !== nodeData?.blockName) {
      updateNodeData(nodeId, { blockName: trimmed });
    }
    onClose();
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      save();
    } else if (e.key === 'Escape') {
      onClose();
    }
  };

  return createPortal(
    <input
      ref={inputRef}
      className="fixed z-50 rounded border px-2 py-1 text-sm shadow-lg outline-none"
      style={{
        left: x,
        top: y,
        backgroundColor: 'var(--color-surface)',
        borderColor: 'var(--color-primary)',
        color: 'var(--color-text)',
        minWidth: 160,
      }}
      value={value}
      onChange={(e) => setValue(e.target.value)}
      onKeyDown={handleKeyDown}
      onBlur={save}
    />,
    document.body
  );
}
