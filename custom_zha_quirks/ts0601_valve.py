"""Royal Gardineer Tuya Water Valve device."""

from zigpy.profiles import zha
from zigpy.quirks import CustomDevice
from zigpy.quirks.v2 import add_to_registry_v2
from zigpy.quirks.v2.homeassistant import EntityPlatform, UnitOfTime, EntityType
import zigpy.types as t
from zigpy.zcl.clusters.general import Basic, Groups, Ota, Scenes, Time
from zigpy.zcl.clusters.smartenergy import Metering

from zhaquirks.tuya import TuyaLocalCluster
from zhaquirks.tuya.mcu import (
    DPToAttributeMapping,
    TuyaMCUCluster,
    TuyaOnOff,
    TuyaPowerConfigurationCluster,
)

# Timer time left to auto-off.
TIMER_TIME_LEFT_ATTR_ID = 0xEF01
TIMER_TIME_LEFT_ATTR_NAME = "timer_time_left"

# Timer state.
TIMER_STATE_ATTR_ID = 0xEF02
TIMER_STATE_ATTR_NAME = "timer_state"

# Last valve open duration.
LAST_VALVE_OPEN_DURATION_ATTR_ID = 0xEF03
LAST_VALVE_OPEN_DURATION_ATTR_NAME = "last_valve_open_duration"

# Weather delay.
WEATHER_DELAY_ATTR_ID = 0xEF04
WEATHER_DELAY_ATTR_NAME = "weather_delay"

class RoyalGardineerWeatherDelay(t.enum8):
    """Royal Gardineer weather delay enum."""

    Disabled = 0x00
    Delayed_24h = 0x01
    Delayed_48h = 0x02
    Delayed_72h = 0x03

class RoyalGardineerTimerState(t.enum8):
    """Royal Gardineer timer state enum."""

    Disabled = 0x00
    Active = 0x01
    Enabled = 0x02

class RoyalGardineerValveWaterConsumed(Metering, TuyaLocalCluster):
    """Royal Gardineer Tuya Water Valve - water consumed cluster."""

    UNIT_VOLUME_LITERS = 0x0007
    TYPE_WATER_METERING = 0x02

    """Setting unit of measurement."""
    _CONSTANT_ATTRIBUTES = {
        0x0300: UNIT_VOLUME_LITERS,
        0x0306: TYPE_WATER_METERING,
    }


class RoyalGardineerValveManufCluster(TuyaMCUCluster):
    """On/Off Royal Gardineer Tuya cluster with extra device attributes."""

    attributes = TuyaMCUCluster.attributes.copy()
    attributes.update(
        {
            TIMER_TIME_LEFT_ATTR_ID: (TIMER_TIME_LEFT_ATTR_NAME, t.uint32_t, True),
            TIMER_STATE_ATTR_ID: (TIMER_STATE_ATTR_NAME, RoyalGardineerTimerState, True),
            LAST_VALVE_OPEN_DURATION_ATTR_ID: (LAST_VALVE_OPEN_DURATION_ATTR_NAME, t.uint32_t, True),
            WEATHER_DELAY_ATTR_ID: (WEATHER_DELAY_ATTR_NAME, RoyalGardineerWeatherDelay, True)
        }
    )

    dp_to_attribute: dict[int, DPToAttributeMapping] = {
        1: DPToAttributeMapping(
            TuyaOnOff.ep_attribute,
            "on_off",
        ),
        5: DPToAttributeMapping(
            RoyalGardineerValveWaterConsumed.ep_attribute,
            "current_summ_delivered",
            lambda x: x // 10,
        ),
        7: DPToAttributeMapping(
            TuyaPowerConfigurationCluster.ep_attribute,
            "battery_percentage_remaining",
        ),
        10: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "weather_delay",
            lambda x: RoyalGardineerWeatherDelay(x),
        ),
        11: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "timer_time_left",
            lambda x: x // 60,
            lambda x: x * 60,
        ),
        12: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "timer_state",
            lambda x: RoyalGardineerTimerState(x),
        ),
        15: DPToAttributeMapping(
            TuyaMCUCluster.ep_attribute,
            "last_valve_open_duration",
            lambda x: x // 60,
        ),
        #16 - cycle timer,
        #17 - normal timer,
    }

    data_point_handlers = {
        1: "_dp_2_attr_update",
        5: "_dp_2_attr_update",
        7: "_dp_2_attr_update",
        10: "_dp_2_attr_update",
        11: "_dp_2_attr_update",
        12: "_dp_2_attr_update",
        15: "_dp_2_attr_update",
    }

(
    add_to_registry_v2("_TZE200_2wg5qrjy", "TS0601")
    .replaces(RoyalGardineerValveManufCluster)
    .adds(TuyaOnOff)
    .adds(RoyalGardineerValveWaterConsumed)
    .adds(TuyaPowerConfigurationCluster)
    # Timer time left/remaining.
    .number(
        TIMER_TIME_LEFT_ATTR_NAME,
        RoyalGardineerValveManufCluster.cluster_id,
        min_value=1,
        max_value=600,
        step=1,
        unit=UnitOfTime.MINUTES,
        translation_key="timer_time_left",
    )
    # Weather delay.
    .enum(
        WEATHER_DELAY_ATTR_NAME,
        RoyalGardineerWeatherDelay,
        RoyalGardineerValveManufCluster.cluster_id,
        translation_key="weather_delay",
    )
    # Timer state - read-only.
    .enum(
        TIMER_STATE_ATTR_NAME,
        RoyalGardineerTimerState,
        RoyalGardineerValveManufCluster.cluster_id,
        entity_platform=EntityPlatform.SENSOR,
        entity_type=EntityType.DIAGNOSTIC,
        translation_key="timer_state",
    )
    # Last valve open duration - read-only.
    .sensor(
        LAST_VALVE_OPEN_DURATION_ATTR_NAME,
        RoyalGardineerValveManufCluster.cluster_id,
        entity_type=EntityType.DIAGNOSTIC,
        unit=UnitOfTime.MINUTES,
        translation_key="last_valve_open_duration",
    )
)
