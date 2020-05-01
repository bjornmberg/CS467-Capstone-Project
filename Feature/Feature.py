'''
Implementation of the Feature class. A feature is an object that exists within a room (example: couch, drawer, etc).
There are three descriptions of the Feature:
    pre_action_des: used when 'look'-ing and the Feature prior to interaction
    in_action_des: used when interacting with the Feature
    post_action_des: used when the feature can no longer be interacted with
    Example:
        pre_action: "The couch's cushions look lumpy there might be something there..."
        in_action: "You see a key lying where the cushions were..."
        post_action: "This is the couch where you found the key..."

    The Feature's state is what dictates the above behavior:
        0 - pre_action
        1 - in_action
        3 - post_action

    The feature_id is an integer that is used to place the Feature into the feature list() within
    the Room object at a specified location. This is important for interactions as Items can be tied
    to the Feature and they need to know which Feature to modify
'''
class Feature:

    # constructor for the Feature class
    def __init__(self, name, pre_action_des, in_action_des, post_action_des, actionable, usable, state, feature_id):

        self.name = name
        self.pre_action_des = pre_action_des
        self.in_action_des = in_action_des
        self.post_action_des = post_action_des
        self.actionable = actionable
        self.usable = usable
        self.state = state
        self.feature_id = feature_id

    def __repr__(self):
        return self


    # checks the state of the feature and returns the appropriate description
    def get_description(self):

        if self.state == 0:
            return self.pre_action_des
        elif self.state == 1:
            return self.in_action_des
        else:
            return self.post_action_des

