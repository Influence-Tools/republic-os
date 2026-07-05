---
type: Jurisdiction
title: "Travis County, TX"
classification: county
fips: "48453"
state: "TX"
demographics:
  population: 1330015
  population_under_18: 268138
  population_18_64: 915472
  population_65_plus: 146405
  median_household_income: 99611
  poverty_rate: 10.93
  homeownership_rate: 52.11
  unemployment_rate: 4.56
  median_home_value: 523000
  gini_index: 0.4851
  vacancy_rate: 5.58
  race_white: 729783
  race_black: 108536
  race_asian: 106667
  race_native: 10618
  hispanic: 433057
  bachelors_plus: 736330
districts:
  - to: "us/states/tx/districts/10"
    rel: in-district
    area_weight: 0.4029
  - to: "us/states/tx/districts/35"
    rel: in-district
    area_weight: 0.2822
  - to: "us/states/tx/districts/37"
    rel: in-district
    area_weight: 0.2064
  - to: "us/states/tx/districts/17"
    rel: in-district
    area_weight: 0.0626
  - to: "us/states/tx/districts/21"
    rel: in-district
    area_weight: 0.0454
  - to: "us/states/tx/districts/senate/14"
    rel: in-district
    area_weight: 0.5075
  - to: "us/states/tx/districts/senate/25"
    rel: in-district
    area_weight: 0.328
  - to: "us/states/tx/districts/senate/21"
    rel: in-district
    area_weight: 0.1645
  - to: "us/states/tx/districts/house/19"
    rel: in-district
    area_weight: 0.2413
  - to: "us/states/tx/districts/house/46"
    rel: in-district
    area_weight: 0.2212
  - to: "us/states/tx/districts/house/47"
    rel: in-district
    area_weight: 0.1958
  - to: "us/states/tx/districts/house/51"
    rel: in-district
    area_weight: 0.1693
  - to: "us/states/tx/districts/house/48"
    rel: in-district
    area_weight: 0.0833
  - to: "us/states/tx/districts/house/50"
    rel: in-district
    area_weight: 0.0542
  - to: "us/states/tx/districts/house/49"
    rel: in-district
    area_weight: 0.0348
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Travis County, TX

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1330015 |
| Under 18 | 268138 |
| 18–64 | 915472 |
| 65+ | 146405 |
| Median household income | 99611 |
| Poverty rate | 10.93 |
| Homeownership rate | 52.11 |
| Unemployment rate | 4.56 |
| Median home value | 523000 |
| Gini index | 0.4851 |
| Vacancy rate | 5.58 |
| White | 729783 |
| Black | 108536 |
| Asian | 106667 |
| Native | 10618 |
| Hispanic/Latino | 433057 |
| Bachelor's or higher | 736330 |

## Districts

- [TX-10](/us/states/tx/districts/10.md) — 40% (congressional)
- [TX-35](/us/states/tx/districts/35.md) — 28% (congressional)
- [TX-37](/us/states/tx/districts/37.md) — 21% (congressional)
- [TX-17](/us/states/tx/districts/17.md) — 6% (congressional)
- [TX-21](/us/states/tx/districts/21.md) — 5% (congressional)
- [TX Senate District 14](/us/states/tx/districts/senate/14.md) — 51% (state senate)
- [TX Senate District 25](/us/states/tx/districts/senate/25.md) — 33% (state senate)
- [TX Senate District 21](/us/states/tx/districts/senate/21.md) — 16% (state senate)
- [TX House District 19](/us/states/tx/districts/house/19.md) — 24% (state house)
- [TX House District 46](/us/states/tx/districts/house/46.md) — 22% (state house)
- [TX House District 47](/us/states/tx/districts/house/47.md) — 20% (state house)
- [TX House District 51](/us/states/tx/districts/house/51.md) — 17% (state house)
- [TX House District 48](/us/states/tx/districts/house/48.md) — 8% (state house)
- [TX House District 50](/us/states/tx/districts/house/50.md) — 5% (state house)
- [TX House District 49](/us/states/tx/districts/house/49.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
