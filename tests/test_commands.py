import unittest
from unittest.mock import patch, MagicMock
from toolkit import commands, config

class TestCommands(unittest.TestCase):

    def setUp(self):
        self.lang_config = {
            "lang_code": "en",
            "idioma_nome": "English",
            "explicacoes": {
                "1": "Test explanation 1",
                "2": "Test explanation 2",
                "3": "Test explanation 3",
                "4": "Test explanation 4",
                "5": "Test explanation 5",
                "6": "Test explanation 6"
            },
            "perguntas": {
                "prompt": "Test prompt",
                "url_video": "Test video prompt",
                "url_site": "Test site prompt"
            },
            "mensagens": {
                "resposta_ia": "Test AI response",
                "erro_execucao": "Test error",
                "limpou_contexto": "Context cleared.",
                "limpou_sessao": "Session reset."
            }
        }
        # Also patch the config module that is imported in commands.py
        self.config_patcher = patch('toolkit.commands.config', AI_MODEL='test-model')
        self.mock_config = self.config_patcher.start()

    def tearDown(self):
        self.config_patcher.stop()

    @patch('builtins.input', return_value='test input')
    @patch('toolkit.utils.executar_comando')
    def test_entrada_manual(self, mock_executar_comando, mock_input):
        # Arrange
        mock_executar_comando.return_value = ("Test output", "", 0)

        # Act
        commands.entrada_manual(self.lang_config)

        # Assert
        mock_input.assert_called_once_with(self.lang_config["perguntas"]["prompt"])
        expected_cmd = ["fabric", "--model", "test-model", "-sp", "extract_wisdom", "-v", "#lang:en #input:test input"]
        mock_executar_comando.assert_called_once_with(expected_cmd)

    @patch('builtins.input', return_value='http://youtube.com/test')
    @patch('toolkit.utils.executar_comando')
    def test_transcrever_video_youtube(self, mock_executar_comando, mock_input):
        # Arrange
        mock_executar_comando.return_value = ("Test output", "", 0)

        # Act
        commands.transcrever_video_youtube(self.lang_config)

        # Assert
        mock_input.assert_called_once_with(self.lang_config["perguntas"]["url_video"])
        expected_cmd = ["fabric", "--youtube=http://youtube.com/test", "--model", "test-model", "-sp", "extract_wisdom", "-v", "#lang:en"]
        mock_executar_comando.assert_called_once_with(expected_cmd)

    @patch('builtins.input', return_value='http://example.com')
    @patch('toolkit.utils.executar_comando')
    def test_scrape_site(self, mock_executar_comando, mock_input):
        # Arrange
        mock_executar_comando.return_value = ("Test output", "", 0)

        # Act
        commands.scrape_site(self.lang_config)

        # Assert
        mock_input.assert_called_once_with(self.lang_config["perguntas"]["url_site"])
        expected_cmd = ["fabric", "--model", "test-model", "-u", "http://example.com", "-sp", "extract_wisdom", "-v", "#lang:en"]
        mock_executar_comando.assert_called_once_with(expected_cmd)

    @patch('toolkit.utils.executar_comando')
    def test_listar_padroes(self, mock_executar_comando):
        # Arrange
        mock_executar_comando.return_value = ("Test output", "", 0)

        # Act
        commands.listar_padroes(self.lang_config)

        # Assert
        expected_cmd = ["fabric", "--listpatterns"]
        mock_executar_comando.assert_called_once_with(expected_cmd)

    @patch('toolkit.utils.executar_comando')
    def test_limpar_contexto(self, mock_executar_comando):
        # Arrange
        mock_executar_comando.return_value = ("", "", 0)

        # Act
        commands.limpar_contexto(self.lang_config)

        # Assert
        expected_cmd = ["fabric", "--wipecontext"]
        mock_executar_comando.assert_called_once_with(expected_cmd)

    @patch('toolkit.utils.executar_comando')
    def test_limpar_sessao(self, mock_executar_comando):
        # Arrange
        mock_executar_comando.return_value = ("", "", 0)

        # Act
        commands.limpar_sessao(self.lang_config)

        # Assert
        expected_cmd = ["fabric", "--wipesession"]
        mock_executar_comando.assert_called_once_with(expected_cmd)

if __name__ == '__main__':
    unittest.main()
