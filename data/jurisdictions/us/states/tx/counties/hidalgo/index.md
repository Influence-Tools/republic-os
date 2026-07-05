---
type: Jurisdiction
title: "Hidalgo County, TX"
classification: county
fips: "48215"
state: "TX"
demographics:
  population: 891977
  population_under_18: 276245
  population_18_64: 511197
  population_65_plus: 104535
  median_household_income: 54338
  poverty_rate: 26.67
  homeownership_rate: 67.46
  unemployment_rate: 7.61
  median_home_value: 140900
  gini_index: 0.4769
  vacancy_rate: 12.43
  race_white: 247551
  race_black: 6207
  race_asian: 9202
  race_native: 3751
  hispanic: 819984
  bachelors_plus: 140423
districts:
  - to: "us/states/tx/districts/15"
    rel: in-district
    area_weight: 0.8063
  - to: "us/states/tx/districts/34"
    rel: in-district
    area_weight: 0.1907
  - to: "us/states/tx/districts/senate/20"
    rel: in-district
    area_weight: 0.7102
  - to: "us/states/tx/districts/senate/27"
    rel: in-district
    area_weight: 0.2893
  - to: "us/states/tx/districts/house/35"
    rel: in-district
    area_weight: 0.6008
  - to: "us/states/tx/districts/house/40"
    rel: in-district
    area_weight: 0.1473
  - to: "us/states/tx/districts/house/39"
    rel: in-district
    area_weight: 0.1415
  - to: "us/states/tx/districts/house/36"
    rel: in-district
    area_weight: 0.0692
  - to: "us/states/tx/districts/house/41"
    rel: in-district
    area_weight: 0.0406
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Hidalgo County, TX

County jurisdiction — 9 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 891977 |
| Under 18 | 276245 |
| 18–64 | 511197 |
| 65+ | 104535 |
| Median household income | 54338 |
| Poverty rate | 26.67 |
| Homeownership rate | 67.46 |
| Unemployment rate | 7.61 |
| Median home value | 140900 |
| Gini index | 0.4769 |
| Vacancy rate | 12.43 |
| White | 247551 |
| Black | 6207 |
| Asian | 9202 |
| Native | 3751 |
| Hispanic/Latino | 819984 |
| Bachelor's or higher | 140423 |

## Districts

- [TX-15](/us/states/tx/districts/15.md) — 81% (congressional)
- [TX-34](/us/states/tx/districts/34.md) — 19% (congressional)
- [TX Senate District 20](/us/states/tx/districts/senate/20.md) — 71% (state senate)
- [TX Senate District 27](/us/states/tx/districts/senate/27.md) — 29% (state senate)
- [TX House District 35](/us/states/tx/districts/house/35.md) — 60% (state house)
- [TX House District 40](/us/states/tx/districts/house/40.md) — 15% (state house)
- [TX House District 39](/us/states/tx/districts/house/39.md) — 14% (state house)
- [TX House District 36](/us/states/tx/districts/house/36.md) — 7% (state house)
- [TX House District 41](/us/states/tx/districts/house/41.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
