
__all__ = ['_const']

class _const:

    class __ConstError(TypeError):
        """修改常量抛出的错误"""
        pass
    def __init__(self):
        """初始化配置"""
        
    def __setattr__(self, __name: str, __value: any) -> None:
        if self.__dict__.has_key(__name):
            raise self.__ConstError(f'修改常量{__name}被阻止')
        
        self.__dict__[__name] = __value


