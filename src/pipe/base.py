"""
"""
import unidecode
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import TfidfVectorizer

    
class TextProcessing(BaseEstimator, TransformerMixin):
    """This processing module is responsible to convert the 
    text features, into numerical features using TfidfVectorizer
    with a sklearn Pipeline base structure.
    """
    
    def __init__(self):
        self._TEXT_COLUMNS = ["query", "title", "concatenated_tags"]
        self._MODEL = TfidfVectorizer()
        self._BUILD = False
    
    @staticmethod
    def _build_text_dataframe(X, columns):
        """Build the text dataframe by joining all text 
        features into one single feature.
        
        :param pd.DataFrame X: Dataframe with text feature data.
        :param list columns: The list of columns to be merged.
        
        :return: A Series with only the joint text columns.
        :rtype: pd.Series
        """
        text_features_df = pd.DataFrame()
        for col in columns:
            if text_features_df.shape[0] > 0:
                text_features_df += X[col]
            else:
                initial_col = col
                text_features_df = X[col]
        text_features_df.fillna('', inplace=True)
        text_features_df = text_features_df.apply(
            lambda t: unidecode.unidecode(t))
        return text_features_df
    
    def fit(self, X, y=None):
        """Fit the TfidfVectorizer model into the text features
        presented in `X` and mapped in `_TEXT_COLUMNS`.
        
        :param pd.DataFrame X: Dataframe with text feature data.
        :param pd.Series y: Series with labels.
        
        :return: This class.
        :rtype: TextProcessing
        """
        text_features_df = TextProcessing._build_text_dataframe(
            X, self._TEXT_COLUMNS)
        self._MODEL.fit(text_features_df)
        self._BUILD = True
        return self

    def transform(self, X):
        """Transform the provided Dataframe using the trained
        TfidfVectorizer already trained.
        
        :param pd.DataFrame X: Dataframe with data to be processed.
        
        :return: Dataframe without text columns, and with numerical features included.
        :rtype: pd.DataFrame
        """
        if self._BUILD:
            X.reset_index(drop=True, inplace=True)
            text_features_df = self._build_text_dataframe(
                X, self._TEXT_COLUMNS)
            text_features_data = self._MODEL.transform(text_features_df)
            text_features_df = pd.DataFrame(data=text_features_data.todense(),
                                            columns=self._MODEL.get_feature_names())
            X.drop(columns = self._TEXT_COLUMNS, inplace=True)
            res_df = pd.concat([X, text_features_df], axis=1)
            return res_df
        else:
            raise Exception("Model is not trained.")
    
    def fit_transform(self, X, y=None):
        """Train the TfidfVectorizer based on the provided data
        and also process the provided data using the trained model.
        
        :param pd.DataFrame X: Dataframe with text feature data.
        :param pd.Series y: Series with labels.
        
        :return: Dataframe without text columns, and with numerical features included.
        :rtype: pd.DataFrame
        """
        self.fit(X, y)
        return self.transform(X)
    
class DateProcessing(BaseEstimator, TransformerMixin):
    """Date processing module, used to create/manipulate date based 
    features with a sklearn Pipeline base structure.
    """
    _DATE_COLUMN = 'creation_date'
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        """Apply the date tranformation on date columns of the
        provided Dataframe.
        
        :param pd.DataFrame X: Dataframe with data to be processed.
        
        :return: Dataframe withouth date columns and new numerical features.
        :rtype: pd.DataFrame
        """
        X['day'] = X[self._DATE_COLUMN].apply(lambda x: x.day)
        X['month'] = X[self._DATE_COLUMN].apply(lambda x: x.month)
        X['year'] = X[self._DATE_COLUMN].apply(lambda x: x.year)
        X.drop(columns=[self._DATE_COLUMN], inplace=True)
        return X
    
    def fit_transform(self, X, y=None):
        """Apply the date tranformation on date columns of the
        provided Dataframe.
        
        :param pd.DataFrame X: Dataframe with data to be processed.
        
        :return: Dataframe withouth date columns and new numerical features.
        :rtype: pd.DataFrame
        """
        return self.transform(X)

class OverallProcessing(BaseEstimator, TransformerMixin):
    """This method exists to condense mild feature processings
    such as removing NaN values, removing undisered columns, and
    so on, using the sklearn Pipeline base structure.
    """
    
    def fit(self, X, y=None):
        """There is no process here."""
        return self
    
    def transform(self, X):
        """Transform the provided Dataframe.
        
        :param pd.DataFrame X: Dataframe with data to be processed.
        
        :return: Dataframe with processed data.
        :rtype: pd.DataFrame
        """
        X.fillna(0.0, inplace=True)
        return X
    
    def fit_transform(self, X, y=None):
        """Transform the provided Dataframe.
        
        :param pd.DataFrame X: Dataframe with data to be processed.
        
        :return: Dataframe with processed data.
        :rtype: pd.DataFrame
        """
        return self.transform(X)