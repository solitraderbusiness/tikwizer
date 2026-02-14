import { create } from 'zustand';
import type { Variable, Constant, ProjectOptions } from '../types';

interface StrategyState {
  name: string;
  variables: Variable[];
  constants: Constant[];
  projectOptions: ProjectOptions;

  setName: (name: string) => void;
  setVariables: (vars: Variable[]) => void;
  setConstants: (consts: Constant[]) => void;
  setProjectOptions: (opts: ProjectOptions) => void;
  addVariable: (v: Variable) => void;
  removeVariable: (id: string) => void;
  addConstant: (c: Constant) => void;
  removeConstant: (id: string) => void;
}

const defaultProjectOptions: ProjectOptions = {
  magic_and_other: { magic_number: '55225', expiration_date: ' ', on_timer_period: '600' },
  pip_size: { rules: '0.001 = 0.015\n0.016 = 0.0001\n0.000001 = 0.0001\n' },
  description_and_version_number: { copy_right: '', description: '', website_address: '', version_number: '1.0' },
  virtual_stops: { virtual_stops: 'True', virtual_stops_time_out: 0, emergency_stops: 'always', relative_size: 0, add_pips: '100' },
  visual: { display_spread_meter: 'True', display_status_messages: 'False', display_indicators_after_test: 'False' },
};

export const useStrategyStore = create<StrategyState>((set) => ({
  name: 'New Strategy',
  variables: [],
  constants: [],
  projectOptions: defaultProjectOptions,

  setName: (name) => set({ name }),
  setVariables: (variables) => set({ variables }),
  setConstants: (constants) => set({ constants }),
  setProjectOptions: (projectOptions) => set({ projectOptions }),
  addVariable: (v) => set((s) => ({ variables: [...s.variables, v] })),
  removeVariable: (id) => set((s) => ({ variables: s.variables.filter((v) => v.id !== id) })),
  addConstant: (c) => set((s) => ({ constants: [...s.constants, c] })),
  removeConstant: (id) => set((s) => ({ constants: s.constants.filter((c) => c.id !== id) })),
}));
