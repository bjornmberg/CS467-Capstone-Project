class Feature:
    """ Class used to represent a static feature with a Room

    Attributes
    ----------
    name: str
        the name of the Feature
    pre_action_des: str
        describes the Feature prior to interaction
    in_action_des: str
        describes the Feature during interaction
    post_action_des: str
        describes the Feature after interaction
    actionable: bool
        denotes whether a Feature can be interacted with
    usable: bool
        denotes whether an Item can be used on a Feature
    state: int
        manages the state of the Feature
    feature_id: int
        unique identifier of the Feature within the Room

    Methods
    -------
    get_description():
        returns the appropriate description based on Feature state
    save_feature()
        returns dictionary representation of the Feature for saving
    """

    def __init__(self, name, pre_action_des, in_action_des, post_action_des, actionable, usable, state, feature_id):

        """Constructor for the Feature class

        :param str name: the name of the Feature
        :param str pre_action_des: the Features pre-action description
        :param str in_action_des: the Features in-action description
        :param str post_action_des: the Features post-action description
        :param bool actionable: denotes ability to interact with Feature
        :param bool usable: denotes ability to use Item on Feature
        :param int state: denotes state of the Feauture
        :param int feature_id: unique identifier of Feature within Room
        """
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

    def get_description(self):
        """ Provides the description based on Feature state

        :return: str : description of the Feature based on state
        """
        if self.state == 0:
            return self.pre_action_des
        elif self.state == 1:
            return self.in_action_des
        else:
            return self.post_action_des

    def save_feature(self):
        """Provides dict representation of the Feature for saving

        :return: dict : used for saving the Feature
        """
        feature_dict = {
            'name': self.name,
            'preActionDes': self.pre_action_des,
            'inActionDes': self.in_action_des,
            'postActionDes': self.post_action_des,
            'actionable': self.actionable,
            'usable': self.usable,
            'state': self.state,
            'featureId': self.feature_id
        }
        return feature_dict
