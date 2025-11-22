import os
import pytest
from gendiff import generate_diff

FIXTURES_PATH = os.path.join(os.path.dirname(__file__), "fixtures")

def read_fixture(filename):
    path = os.path.join(FIXTURES_PATH, filename)
    with open(path, 'r') as f:
        return f.read().strip()

def test_flat_json():
    file1 = os.path.join(FIXTURES_PATH, "file1.json")
    file2 = os.path.join(FIXTURES_PATH, "file2.json")
    expected = read_fixture("expected_flat.txt")

    result = generate_diff(file1, file2)
    assert result.strip() == expected

def test_flat_yaml():
    file1 = os.path.join(FIXTURES_PATH, "file1.yml")
    file2 = os.path.join(FIXTURES_PATH, "file2.yml")
    expected = read_fixture("expected_yaml.txt")

    result = generate_diff(file1, file2)
    assert result.strip() == expected

def test_mixed_formats():
    """Test que podemos comparar JSON con YAML"""
    json_file = os.path.join(FIXTURES_PATH, "file1.json")
    yaml_file = os.path.join(FIXTURES_PATH, "file1.yml")
    
    # Ambos archivos deberían tener el mismo contenido
    result = generate_diff(json_file, yaml_file)
    # La diferencia debería ser vacía (o casi vacía)
    assert "  - " not in result or "  + " not in result

def test_unsupported_format():
    """Test que verifica el manejo de formatos no soportados"""
    with pytest.raises(ValueError, match="Formato no soportado"):
        generate_diff("file.txt", "file2.json")
