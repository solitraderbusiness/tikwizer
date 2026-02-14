import { describe, it, expect, beforeEach } from 'vitest';
import { useStrategyStore } from './strategyStore';

describe('strategyStore', () => {
  beforeEach(() => {
    useStrategyStore.setState({
      name: 'New Strategy',
      variables: [],
      constants: [],
      projectOptions: {
        magic_and_other: { magic_number: '55225', expiration_date: ' ', on_timer_period: '600' },
        pip_size: { rules: '0.001 = 0.015\n0.016 = 0.0001\n0.000001 = 0.0001\n' },
        description_and_version_number: { copy_right: '', description: '', website_address: '', version_number: '1.0' },
        virtual_stops: { virtual_stops: 'True', virtual_stops_time_out: 0, emergency_stops: 'always', relative_size: 0, add_pips: '100' },
        visual: { display_spread_meter: 'True', display_status_messages: 'False', display_indicators_after_test: 'False' },
      },
    });
  });

  it('has default name', () => {
    expect(useStrategyStore.getState().name).toBe('New Strategy');
  });

  it('sets name', () => {
    useStrategyStore.getState().setName('My EA');
    expect(useStrategyStore.getState().name).toBe('My EA');
  });

  it('starts with empty variables', () => {
    expect(useStrategyStore.getState().variables).toEqual([]);
  });

  it('starts with empty constants', () => {
    expect(useStrategyStore.getState().constants).toEqual([]);
  });

  it('adds a variable', () => {
    const v = { id: 'v1', type: 'double', name: 'myVar', value: '0', description: '' };
    useStrategyStore.getState().addVariable(v);
    expect(useStrategyStore.getState().variables).toHaveLength(1);
    expect(useStrategyStore.getState().variables[0].name).toBe('myVar');
    expect(useStrategyStore.getState().variables[0].type).toBe('double');
    expect(useStrategyStore.getState().variables[0].value).toBe('0');
  });

  it('removes a variable by id', () => {
    const v = { id: 'v1', type: 'double', name: 'myVar', value: '0', description: '' };
    useStrategyStore.getState().addVariable(v);
    expect(useStrategyStore.getState().variables).toHaveLength(1);

    useStrategyStore.getState().removeVariable('v1');
    expect(useStrategyStore.getState().variables).toHaveLength(0);
  });

  it('adds multiple variables', () => {
    const v1 = { id: 'v1', type: 'double', name: 'var1', value: '0', description: '' };
    const v2 = { id: 'v2', type: 'int', name: 'var2', value: '10', description: 'count' };
    useStrategyStore.getState().addVariable(v1);
    useStrategyStore.getState().addVariable(v2);
    expect(useStrategyStore.getState().variables).toHaveLength(2);
    expect(useStrategyStore.getState().variables[0].id).toBe('v1');
    expect(useStrategyStore.getState().variables[1].id).toBe('v2');
  });

  it('removes only the targeted variable', () => {
    const v1 = { id: 'v1', type: 'double', name: 'var1', value: '0', description: '' };
    const v2 = { id: 'v2', type: 'int', name: 'var2', value: '10', description: '' };
    useStrategyStore.getState().addVariable(v1);
    useStrategyStore.getState().addVariable(v2);

    useStrategyStore.getState().removeVariable('v1');
    expect(useStrategyStore.getState().variables).toHaveLength(1);
    expect(useStrategyStore.getState().variables[0].id).toBe('v2');
  });

  it('adds a constant', () => {
    const c = { id: 'c1', type: 'int', name: 'MAX', value: '100', description: 'max val' };
    useStrategyStore.getState().addConstant(c);
    expect(useStrategyStore.getState().constants).toHaveLength(1);
    expect(useStrategyStore.getState().constants[0].name).toBe('MAX');
    expect(useStrategyStore.getState().constants[0].value).toBe('100');
  });

  it('removes a constant by id', () => {
    const c = { id: 'c1', type: 'int', name: 'MAX', value: '100', description: 'max val' };
    useStrategyStore.getState().addConstant(c);
    expect(useStrategyStore.getState().constants).toHaveLength(1);

    useStrategyStore.getState().removeConstant('c1');
    expect(useStrategyStore.getState().constants).toHaveLength(0);
  });

  it('removes only the targeted constant', () => {
    const c1 = { id: 'c1', type: 'int', name: 'MAX', value: '100', description: '' };
    const c2 = { id: 'c2', type: 'string', name: 'PREFIX', value: 'EA_', description: '' };
    useStrategyStore.getState().addConstant(c1);
    useStrategyStore.getState().addConstant(c2);

    useStrategyStore.getState().removeConstant('c1');
    expect(useStrategyStore.getState().constants).toHaveLength(1);
    expect(useStrategyStore.getState().constants[0].id).toBe('c2');
  });

  it('sets variables array directly', () => {
    const vars = [
      { id: 'v1', type: 'double', name: 'a', value: '1', description: '' },
      { id: 'v2', type: 'int', name: 'b', value: '2', description: '' },
    ];
    useStrategyStore.getState().setVariables(vars);
    expect(useStrategyStore.getState().variables).toEqual(vars);
  });

  it('sets constants array directly', () => {
    const consts = [
      { id: 'c1', type: 'int', name: 'X', value: '42', description: '' },
    ];
    useStrategyStore.getState().setConstants(consts);
    expect(useStrategyStore.getState().constants).toEqual(consts);
  });

  it('has default project options', () => {
    const opts = useStrategyStore.getState().projectOptions;
    expect(opts.magic_and_other.magic_number).toBe('55225');
    expect(opts.magic_and_other.expiration_date).toBe(' ');
    expect(opts.magic_and_other.on_timer_period).toBe('600');
    expect(opts.virtual_stops.virtual_stops).toBe('True');
    expect(opts.virtual_stops.virtual_stops_time_out).toBe(0);
    expect(opts.virtual_stops.emergency_stops).toBe('always');
    expect(opts.virtual_stops.relative_size).toBe(0);
    expect(opts.virtual_stops.add_pips).toBe('100');
    expect(opts.description_and_version_number.version_number).toBe('1.0');
    expect(opts.description_and_version_number.copy_right).toBe('');
    expect(opts.description_and_version_number.description).toBe('');
    expect(opts.description_and_version_number.website_address).toBe('');
    expect(opts.visual.display_spread_meter).toBe('True');
    expect(opts.visual.display_status_messages).toBe('False');
    expect(opts.visual.display_indicators_after_test).toBe('False');
  });

  it('has default pip_size rules', () => {
    const opts = useStrategyStore.getState().projectOptions;
    expect(opts.pip_size.rules).toContain('0.001 = 0.015');
    expect(opts.pip_size.rules).toContain('0.016 = 0.0001');
  });

  it('updates project options', () => {
    const opts = useStrategyStore.getState().projectOptions;
    useStrategyStore.getState().setProjectOptions({
      ...opts,
      magic_and_other: { ...opts.magic_and_other, magic_number: '99999' },
    });
    expect(useStrategyStore.getState().projectOptions.magic_and_other.magic_number).toBe('99999');
    // Other fields should be unchanged
    expect(useStrategyStore.getState().projectOptions.virtual_stops.virtual_stops).toBe('True');
  });

  it('updates project options preserving unmodified sections', () => {
    const opts = useStrategyStore.getState().projectOptions;
    useStrategyStore.getState().setProjectOptions({
      ...opts,
      visual: { ...opts.visual, display_spread_meter: 'False' },
    });
    expect(useStrategyStore.getState().projectOptions.visual.display_spread_meter).toBe('False');
    expect(useStrategyStore.getState().projectOptions.magic_and_other.magic_number).toBe('55225');
  });
});
