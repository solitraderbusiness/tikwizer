import { memo } from 'react';
import { Position, type NodeProps } from '@xyflow/react';
import { BaseNode } from './BaseNode';
import type { FlowNodeData } from '../../../types';

function ConditionNodeInner({ data, selected, id }: NodeProps) {
  const nodeData = data as unknown as FlowNodeData;
  const operator = nodeData.params?.operator?.label || '?';

  return (
    <BaseNode
      data={nodeData}
      selected={selected}
      id={id}
      outputHandles={[
        { id: 'blue', position: Position.Right, color: '#3b82f6', label: 'True' },
        { id: 'red', position: Position.Bottom, color: '#ef4444', label: 'False' },
      ]}
    >
      <div className="text-center">
        <span className="font-mono text-sm">{operator}</span>
      </div>
    </BaseNode>
  );
}

export const ConditionNode = memo(ConditionNodeInner);
