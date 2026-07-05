---
type: Jurisdiction
title: "Sandoval County, NM"
classification: county
fips: "35043"
state: "NM"
demographics:
  population: 153604
  population_under_18: 33391
  population_18_64: 89408
  population_65_plus: 30805
  median_household_income: 86636
  poverty_rate: 9.96
  homeownership_rate: 83.54
  unemployment_rate: 5.18
  median_home_value: 313800
  gini_index: 0.4224
  vacancy_rate: 6.61
  race_white: 78213
  race_black: 3501
  race_asian: 2084
  race_native: 18548
  hispanic: 61448
  bachelors_plus: 51205
districts:
  - to: "us/states/nm/districts/03"
    rel: in-district
    area_weight: 0.8966
  - to: "us/states/nm/districts/01"
    rel: in-district
    area_weight: 0.1034
  - to: "us/states/nm/districts/senate/22"
    rel: in-district
    area_weight: 0.8527
  - to: "us/states/nm/districts/senate/40"
    rel: in-district
    area_weight: 0.0779
  - to: "us/states/nm/districts/senate/9"
    rel: in-district
    area_weight: 0.0384
  - to: "us/states/nm/districts/senate/19"
    rel: in-district
    area_weight: 0.0279
  - to: "us/states/nm/districts/house/65"
    rel: in-district
    area_weight: 0.6133
  - to: "us/states/nm/districts/house/43"
    rel: in-district
    area_weight: 0.1975
  - to: "us/states/nm/districts/house/41"
    rel: in-district
    area_weight: 0.0569
  - to: "us/states/nm/districts/house/57"
    rel: in-district
    area_weight: 0.0539
  - to: "us/states/nm/districts/house/50"
    rel: in-district
    area_weight: 0.045
  - to: "us/states/nm/districts/house/60"
    rel: in-district
    area_weight: 0.024
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Sandoval County, NM

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 153604 |
| Under 18 | 33391 |
| 18–64 | 89408 |
| 65+ | 30805 |
| Median household income | 86636 |
| Poverty rate | 9.96 |
| Homeownership rate | 83.54 |
| Unemployment rate | 5.18 |
| Median home value | 313800 |
| Gini index | 0.4224 |
| Vacancy rate | 6.61 |
| White | 78213 |
| Black | 3501 |
| Asian | 2084 |
| Native | 18548 |
| Hispanic/Latino | 61448 |
| Bachelor's or higher | 51205 |

## Districts

- [NM-03](/us/states/nm/districts/03.md) — 90% (congressional)
- [NM-01](/us/states/nm/districts/01.md) — 10% (congressional)
- [NM Senate District 22](/us/states/nm/districts/senate/22.md) — 85% (state senate)
- [NM Senate District 40](/us/states/nm/districts/senate/40.md) — 8% (state senate)
- [NM Senate District 9](/us/states/nm/districts/senate/9.md) — 4% (state senate)
- [NM Senate District 19](/us/states/nm/districts/senate/19.md) — 3% (state senate)
- [NM House District 65](/us/states/nm/districts/house/65.md) — 61% (state house)
- [NM House District 43](/us/states/nm/districts/house/43.md) — 20% (state house)
- [NM House District 41](/us/states/nm/districts/house/41.md) — 6% (state house)
- [NM House District 57](/us/states/nm/districts/house/57.md) — 5% (state house)
- [NM House District 50](/us/states/nm/districts/house/50.md) — 4% (state house)
- [NM House District 60](/us/states/nm/districts/house/60.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
