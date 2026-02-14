import { memo, type ReactNode } from 'react';
import { Handle, Position } from '@xyflow/react';
import type { FlowNodeData } from '../../../types';
import { useEditorStore } from '../../../stores/editorStore';

interface BaseNodeProps {
  data: FlowNodeData;
  selected?: boolean;
  id: string;
  children?: ReactNode;
  outputHandles?: Array<{ id: string; position: Position; color: string; label?: string }>;
}

function BaseNodeInner({ data, selected, id, children, outputHandles = [] }: BaseNodeProps) {
  const setSelectedNode = useEditorStore((s) => s.setSelectedNode);
  const updateNodeData = useEditorStore((s) => s.updateNodeData);

  return (
    <div
      onClick={() => setSelectedNode(id)}
      className="rounded-lg shadow-lg min-w-[180px]"
      style={{
        backgroundColor: 'var(--color-surface)',
        border: `2px solid ${selected ? 'var(--color-primary)' : 'var(--color-border)'}`,
        opacity: data.enabled ? 1 : 0.5,
      }}
    >
      {/* Input handle */}
      <Handle type="target" position={Position.Top} id="c" style={{ background: '#6366f1', width: 10, height: 10 }} />

      {/* Title bar */}
      <div
        className="flex items-center justify-between px-3 py-1.5 rounded-t-md text-sm font-medium"
        style={{ backgroundColor: 'var(--color-surface-light)', color: 'var(--color-text)' }}
      >
        <span className="truncate">{data.blockName}</span>
        <div className="flex items-center gap-1.5 ml-2">
          <span className="text-xs" style={{ color: 'var(--color-text-muted)' }}>#{data.id_by_user}</span>
          <button
            onClick={(e) => {
              e.stopPropagation();
              updateNodeData(id, { enabled: !data.enabled });
            }}
            className="w-4 h-4 rounded-full border flex items-center justify-center text-xs"
            style={{
              borderColor: data.enabled ? 'var(--color-accent-green)' : 'var(--color-accent-red)',
              backgroundColor: data.enabled ? 'var(--color-accent-green)' : 'transparent',
              color: data.enabled ? 'white' : 'var(--color-accent-red)',
            }}
            title={data.enabled ? 'Disable' : 'Enable'}
          >
            {data.enabled ? '✓' : ''}
          </button>
        </div>
      </div>

      {/* Content area */}
      {children && (
        <div className="px-3 py-2 text-xs" style={{ color: 'var(--color-text-muted)' }}>
          {children}
        </div>
      )}

      {/* Output handles */}
      {outputHandles.map((h) => (
        <Handle
          key={h.id}
          type="source"
          position={h.position}
          id={h.id}
          style={{
            background: h.color,
            width: 10,
            height: 10,
            ...(h.position === Position.Bottom ? {} : {}),
          }}
        />
      ))}
    </div>
  );
}

export const BaseNode = memo(BaseNodeInner);
