# Copyright 2020 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for audio specs."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow.compat.v2 as tf
from tensorflow_examples.lite.model_maker.core.task import audio_spec


class BaseSpecTest(tf.test.TestCase):

  def test_unable_to_instantiate_baseclass(self):
    with self.assertRaisesRegex(TypeError, 'Can\'t instantiate abstract class'):
      audio_spec.BaseSpec()


if __name__ == '__main__':
  tf.test.main()
