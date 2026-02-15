import { create } from 'zustand';
import type { Variable, Constant, ProjectOptions } from '../types';

export type SelectedVarConst = { kind: 'variable' | 'constant'; id: string } | null;

interface StrategyState {
  name: string;
  variables: Variable[];
  constants: Constant[];
  projectOptions: ProjectOptions;
  selectedVarConst: SelectedVarConst;

  setName: (name: string) => void;
  setVariables: (vars: Variable[]) => void;
  setConstants: (consts: Constant[]) => void;
  setProjectOptions: (opts: ProjectOptions) => void;
  addVariable: (v: Variable) => void;
  removeVariable: (id: string) => void;
  updateVariable: (id: string, data: Partial<Variable>) => void;
  addConstant: (c: Constant) => void;
  removeConstant: (id: string) => void;
  updateConstant: (id: string, data: Partial<Constant>) => void;
  selectVarConst: (sel: SelectedVarConst) => void;
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
  selectedVarConst: null,

  setName: (name) => set({ name }),
  setVariables: (variables) => set({ variables }),
  setConstants: (constants) => set({ constants }),
  setProjectOptions: (projectOptions) => set({ projectOptions }),
  addVariable: (v) => set((s) => ({ variables: [...s.variables, v] })),
  removeVariable: (id) => set((s) => ({ variables: s.variables.filter((v) => v.id !== id) })),
  updateVariable: (id, data) => set((s) => ({ variables: s.variables.map((v) => v.id === id ? { ...v, ...data } : v) })),
  addConstant: (c) => set((s) => ({ constants: [...s.constants, c] })),
  removeConstant: (id) => set((s) => ({ constants: s.constants.filter((c) => c.id !== id) })),
  updateConstant: (id, data) => set((s) => ({ constants: s.constants.map((c) => c.id === id ? { ...c, ...data } : c) })),
  selectVarConst: (sel) => set({ selectedVarConst: sel }),
}));
