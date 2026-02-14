import { memo } from 'react';
import { Position, type NodeProps } from '@xyflow/react';
import { BaseNode } from './BaseNode';
import type { FlowNodeData } from '../../../types';

function ActionNodeInner({ data, selected, id }: NodeProps) {
  const nodeData = data as unknown as FlowNodeData;
  return (
    <BaseNode
      data={nodeData}
      selected={selected}
      id={id}
      outputHandles={[
        { id: 'blue', position: Position.Bottom, color: '#3b82f6' },
      ]}
    />
  );
}

export const ActionNode = memo(ActionNodeInner);
