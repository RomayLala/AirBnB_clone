import unittest
from models.state import State
from models.base_model import BaseModel
from models import storage  # Make sure to use the correct storage instance

class TestState(unittest.TestCase):
    """Test the State class."""

    def test_state_creation(self):
        """Test creation of State instance."""
        state = State()
        self.assertIsInstance(state, State)
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertEqual(state.name, "")

    def test_state_save(self):
        """Test saving State instance to storage."""
        state = State()
        state.name = "California"
        state.save()
        all_states = storage.all()
        state_key = f"State.{state.id}"
        self.assertIn(state_key, all_states)
        self.assertEqual(all_states[state_key].name, "California")

    def test_state_reload(self):
        """Test reloading State instance from storage."""
        state = State()
        state.name = "Texas"
        state.save()
        all_states = storage.all()
        state_key = f"State.{state.id}"
        self.assertIn(state_key, all_states)

        # Reload the storage (this should be on the storage, not the state object)
        storage.reload()

        # After reloading, check if the state is still present in the storage
        reloaded_state = storage.all().get(state_key)
        self.assertIsNotNone(reloaded_state)  # Ensure the state exists after reload
        self.assertEqual(reloaded_state.name, "Texas")  # Ensure the name is still the same after reload
