from trainers.pipeline import Pipeline


class _Mem:
    def scan(self, _p):
        return None

    def read_int(self, _a):
        return 0

    def write_int(self, _a, _v):
        return None


def test_pipeline_loads_and_ticks():
    cfg = {"memory": {"pattern_ghost_flag": "48 ??", "pattern_trainer_ptr": "48 ??"}}
    pipe = Pipeline(cfg, _Mem())
    pipe.load_stages([
        "trainers.handlers.ghost_scan_handler.GhostScanHandler",
        "trainers.processors.spirit_state_processor.SpiritStateProcessor",
    ])
    pipe.tick()
    assert "ghost_flag_addr" in pipe.state