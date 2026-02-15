export interface NodeParams {
  [key: string]: any;
}

export interface StrategyNode {
  id: string;
  id_by_user: number;
  blockName: string;
  block_name_mql: string;
  category: string;
  params: NodeParams;
  enabled: boolean;
  position?: { x: number; y: number };
}

export interface StrategyEdge {
  id: string;
  source: string;
  sourceHandle: 'blue' | 'red';
  target: string;
  targetHandle: string;
  type?: string;
}

export interface EventData {
  nodes: StrategyNode[];
  edges: StrategyEdge[];
}

export type EventName = 'on_tick' | 'on_init' | 'on_timer' | 'on_trade' | 'on_chart' | 'on_deinit';

export interface StrategyData {
  events: Record<EventName, EventData>;
  variables: Variable[];
  constants: Constant[];
  project_options: ProjectOptions;
}

export interface Variable {
  id: string;
  type: string;
  name: string;
  value: string;
  description: string;
}

export interface Constant {
  id: string;
  type: string;
  name: string;
  value: string;
  description: string;
}

export interface ProjectOptions {
  magic_and_other: {
    magic_number: string;
    expiration_date: string;
    on_timer_period: string;
  };
  pip_size: { rules: string };
  description_and_version_number: {
    copy_right: string;
    description: string;
    website_address: string;
    version_number: string;
  };
  virtual_stops: {
    virtual_stops: string;
    virtual_stops_time_out: number;
    emergency_stops: string;
    relative_size: number;
    add_pips: string;
  };
  visual: {
    display_spread_meter: string;
    display_status_messages: string;
    display_indicators_after_test: string;
  };
}

export interface BlockTemplate {
  name: string;
  display_name: string;
  category: string;
  default_params: NodeParams;
}

export interface BlockCategory {
  category: string;
  blocks: BlockTemplate[];
}

export interface IndicatorTemplate {
  name: string;
  display_name: string;
  default_params: NodeParams;
}

// React Flow custom node data — index signature required by @xyflow/react
export interface FlowNodeData extends Record<string, unknown> {
  blockName: string;
  block_name_mql: string;
  category: string;
  params: NodeParams;
  enabled: boolean;
  id_by_user: number;
}

// Context menu types
export interface ContextMenuPosition {
  x: number;
  y: number;
}

export interface ClipboardNode {
  type: string;
  data: FlowNodeData;
  relativePosition: { x: number; y: number };
}

export interface ClipboardEdge {
  id: string;
  source: string;
  target: string;
  sourceHandle?: string | null;
  targetHandle?: string | null;
  type?: string;
}

export interface ClipboardPayload {
  nodes: ClipboardNode[];
  edges: ClipboardEdge[];
}
