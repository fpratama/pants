# coding=utf-8
# Copyright 2016 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import absolute_import, division, print_function, unicode_literals

from pants_test.jvm.nailgun_task_test_base import NailgunTaskTestBase

from pants.contrib.findbugs.tasks.findbugs import FindBugs


class FindBugsTest(NailgunTaskTestBase):
  @classmethod
  def task_type(cls):
    return FindBugs

  def test_no_sources(self):
    task = self.prepare_execute(self.context())
    self.assertEqual(None, task.execute())
