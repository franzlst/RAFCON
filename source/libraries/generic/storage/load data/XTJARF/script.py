

def execute(self, inputs, outputs, gvm):
    import rafcon.mvc.statemachine_helper as statemachine_helper
    
    # self.parent refers to the Library state, but we want its parent
    state = self.parent.parent
    state_m = statemachine_helper.get_state_model_for_state(state)
    
    # Load the data from the meta data of the next higher root state
    # (either a library or the root state of the state machine)
    root_state_m = statemachine_helper.get_root_state_model(state_m, library_root=True)
    if inputs['key'] in root_state_m.meta['data']:
        outputs['value'] = root_state_m.meta['data'][inputs['key']]
    else:
        outputs['value'] = None
        
    return 0

