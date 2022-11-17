class global_val:
    Id = '0'
    api_name='1'
    request_name = '2'
    url = '3'
    run = '4'
    request_way = '5'
    header = '6'
    case_depend = '7'
    data_depend = '8'
    field_depend = '9'
    data = '10'
    expect = '11'
    result = '12'
    params='13'
    times='14'


def get_id():
    """获取case_id"""
    return global_val.Id
def get_api_name():
    """获取case_id"""
    return global_val.api_name

def get_request_name():
    """获取请求模块名称"""
    return global_val.request_name


def get_url():
    """获取请求url"""
    return global_val.url

#print(get_url())
def get_run():
    """获取是否运行"""
    return global_val.run


def get_run_way():
    """获取请求方式"""
    return global_val.request_way


def get_header():
    """获取是否携带header"""
    return global_val.header


def get_case_depend():
    """case依赖"""
    return global_val.case_depend


def get_data_depend():
    """依赖的返回数据"""
    return global_val.data_depend


def get_field_depend():
    """数据依赖字段"""
    return global_val.field_depend


def get_data():
    """获取请求数据"""
    return eval(global_val.data)


def get_expect():
    """获取预期结果"""
    return global_val.expect


def get_result():
    """获取返回结果"""
    return global_val.result
def get_params():
    """获取返回结果"""
    return eval(global_val.params)
def get_times():
    """获取返回结果"""
    return eval(global_val.times)
