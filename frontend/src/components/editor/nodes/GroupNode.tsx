import { memo } from 'react';
import type { NodeProps } from '@xyflow/react';
import type { FlowNodeData } from '../../../types';

function GroupNodeInner({ data }: NodeProps) {
  const nodeData = data as unknown as FlowNodeData;

  return (
    <div
      className="w-full h-full rounded-lg"
      style={{
        border: '2px dashed var(--color-primary)',
        backgroundColor: 'color-mix(in srgb, var(--color-primary) 5%, transparent)',
        minWidth: '100%',
        minHeight: '100%',
      }}
    >
      <div
        className="absolute -top-6 left-2 text-xs font-medium px-1.5 py-0.5 rounded"
        style={{
          color: 'var(--color-primary)',
          backgroundColor: 'var(--color-surface)',
        }}
      >
        {nodeData.blockName}
      </div>
    </div>
  );
}

export const GroupNode = memo(GroupNodeInner);
