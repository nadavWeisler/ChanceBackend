class Constants:
    UPLOAD_FILE_INPUT = "FILE_INPUT"
    JWT_SECRET_KEY = "JWT_SECRET_KEY"
    MONGODB_SETTINGS = "MONGODB_SETTINGS"


class EnvironmentVariables:
    CONNECTION_STRING = "CONNECTION_STRING"
    SECRET_KEY = "SECRET_KEY"


class Errors:
    LOAD_EXPERIMENT_ERROR = "Experiment load failed"
    ExperimentDoesNotExit = "Experiment does not exit"

    class AuthenticationErrors:
        UserAlreadyExist = "User Already Exist"
        BadEmailOrPassword = "Bad Email or Password"


class Messages:
    UserAddedSuccessfully = "User added successfully"
    LoginSucceeded = "Login Succeeded!"


class BrmsTypes:
    Mix = "mix"
    Random = "random"
    Fix = "fix"


class PluginNames:
    bRMS = "bRMS"
    ImageButton = "image-button-response"


class BrmsProperties:
    SubGroup = "sub_block"
    StimulusDictionary = "StimulusDictionary"
    BrmsType = "brms_type"
    StimulusBlock = "stimulus_block"
    Count = "count"
    File = "file"
    Stimulus = "stimulus"
    Block = "block"
    Type = "type"


class DBTables:
    Users = "Users"
    Experiments = "Experiments"
    Results = "Results"


class ResponseStatus:
    Success = 200
    UserCreated = 201
    Unauthorized = 401
    UserAlreadyExist = 409