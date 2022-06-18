class Procedimiento:
    id=""
    date = ""
    description = ""
    procedure_type_id = 0
    tree_id = 0
    responsible_id = 0
    user_id = 0
    created_at = ""
    updated_at = ""
    midic = dict()

    def __init__(self,p_id,p_date, p_description,p_procedure_type_id,p_tree_id,p_responsible_id,p_user_id,p_created_at,p_updated_at ):
        self.id = p_id
        self.date = p_date  
        self.description = p_description
        self.procedure_type_id = p_procedure_type_id
        self.tree_id = p_tree_id
        self.responsible_id = p_responsible_id
        self.user_id = p_user_id
        self.created_at = p_created_at
        self.updated_at = p_updated_at    

        self.midic["id"]= p_id
        self.midic["date"]= p_date
        self.midic["p_description"] = p_description
        self.midic["procedure_type_id"] = p_procedure_type_id
        self.midic["tree_id"] = p_tree_id
        self.midic["responsible_id"] = p_responsible_id
        self.midic["user_id"] = p_user_id
        self.midic["created_at"] = p_created_at
        self.midic["updated_at"] = p_updated_at 
         

