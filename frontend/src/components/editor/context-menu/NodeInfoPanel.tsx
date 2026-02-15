import { useEffect, useRef } from 'react';
import { createPortal } from 'react-dom';
import { useEditorStore } from '../../../stores/editorStore';
import type { FlowNodeData } from '../../../types';

interface NodeInfoPanelProps {
  nodeId: string;
  x: number;
  y: number;
  onClose: () => void;
}

export function NodeInfoPanel({ nodeId, x, y, onClose }: NodeInfoPanelProps) {
  const nodes = useEditorStore((s) => s.nodes);
  const edges = useEditorStore((s) => s.edges);
  const panelRef = useRef<HTMLDivElement>(null);

  const node = nodes().find((n) => n.id === nodeId);
  const nodeData = node?.data as FlowNodeData | undefined;
  const allEdges = edges();

  const inCount = allEdges.filter((e) => e.target === nodeId).length;
  const outCount = allEdges.filter((e) => e.source === nodeId).length;

  useEffect(() => {
    const handleClick = (e: MouseEvent) => {
      if (panelRef.current && !panelRef.current.contains(e.target as Node)) {
        onClose();
      }
    };
    const handleKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    document.addEventListener('mousedown', handleClick);
    document.addEventListener('keydown', handleKey);
    return () => {
      document.removeEventListener('mousedown', handleClick);
      document.removeEventListener('keydown', handleKey);
    };
  }, [onClose]);

  if (!nodeData) return null;

  const rows = [
    ['Type', node?.type ?? 'unknown'],
    ['Block (MQL)', nodeData.block_name_mql || '-'],
    ['Category', nodeData.category],
    ['User ID', `#${nodeData.id_by_user}`],
    ['Enabled', nodeData.enabled ? 'Yes' : 'No'],
    ['Incoming', String(inCount)],
    ['Outgoing', String(outCount)],
  ];

  return createPortal(
    <div
      ref={panelRef}
      className="fixed z-50 min-w-[220px] rounded-lg p-3 shadow-xl border text-sm"
      style={{
        left: x,
        top: y,
        backgroundColor: 'var(--color-surface)',
        borderColor: 'var(--color-border)',
        color: 'var(--color-text)',
      }}
    >
      <div className="font-medium mb-2" style={{ color: 'var(--color-primary)' }}>
        {nodeData.blockName}
      </div>
      <table className="w-full">
        <tbody>
          {rows.map(([label, val]) => (
            <tr key={label}>
              <td className="pr-3 py-0.5" style={{ color: 'var(--color-text-muted)' }}>{label}</td>
              <td className="py-0.5 text-right">{val}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>,
    document.body
  );
}
