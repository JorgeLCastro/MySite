from main import procedimientos_tipo


class Procedimiento_tipo:
    id = ""
    name = ""
    description = ""
    created_at = ""
    updated_at = ""
    midic = dict()
    

    def __init__(self,p_id,p_name,p_description,p_created_at,p_updated_at ):
        self.id = p_id
        self.name = p_name
        self.p_description = p_description
        self.created_at = p_created_at
        self.updated_at = p_updated_at    

        self.midic["id"]= p_id        
        self.midic["name"]= p_name
        self.midic["p_description"] = p_description
        self.midic["created_at"] = p_created_at
        self.midic["updated_at"] = p_updated_at 
