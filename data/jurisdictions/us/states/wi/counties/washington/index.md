---
type: Jurisdiction
title: "Washington County, WI"
classification: county
fips: "55131"
state: "WI"
demographics:
  population: 137879
  population_under_18: 28925
  population_18_64: 81587
  population_65_plus: 27367
  median_household_income: 96359
  poverty_rate: 5.79
  homeownership_rate: 78.07
  unemployment_rate: 2.55
  median_home_value: 344800
  gini_index: 0.4073
  vacancy_rate: 3.89
  race_white: 126038
  race_black: 1836
  race_asian: 2019
  race_native: 188
  hispanic: 5174
  bachelors_plus: 45596
districts:
  - to: "us/states/wi/districts/05"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/wi/districts/senate/20"
    rel: in-district
    area_weight: 0.6707
  - to: "us/states/wi/districts/senate/33"
    rel: in-district
    area_weight: 0.2528
  - to: "us/states/wi/districts/senate/8"
    rel: in-district
    area_weight: 0.0765
  - to: "us/states/wi/districts/house/59"
    rel: in-district
    area_weight: 0.3564
  - to: "us/states/wi/districts/house/58"
    rel: in-district
    area_weight: 0.3143
  - to: "us/states/wi/districts/house/98"
    rel: in-district
    area_weight: 0.2526
  - to: "us/states/wi/districts/house/22"
    rel: in-district
    area_weight: 0.0441
  - to: "us/states/wi/districts/house/24"
    rel: in-district
    area_weight: 0.0323
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Washington County, WI

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 137879 |
| Under 18 | 28925 |
| 18–64 | 81587 |
| 65+ | 27367 |
| Median household income | 96359 |
| Poverty rate | 5.79 |
| Homeownership rate | 78.07 |
| Unemployment rate | 2.55 |
| Median home value | 344800 |
| Gini index | 0.4073 |
| Vacancy rate | 3.89 |
| White | 126038 |
| Black | 1836 |
| Asian | 2019 |
| Native | 188 |
| Hispanic/Latino | 5174 |
| Bachelor's or higher | 45596 |

## Districts

- [WI-05](/us/states/wi/districts/05.md) — 100% (congressional)
- [WI Senate District 20](/us/states/wi/districts/senate/20.md) — 67% (state senate)
- [WI Senate District 33](/us/states/wi/districts/senate/33.md) — 25% (state senate)
- [WI Senate District 8](/us/states/wi/districts/senate/8.md) — 8% (state senate)
- [WI House District 59](/us/states/wi/districts/house/59.md) — 36% (state house)
- [WI House District 58](/us/states/wi/districts/house/58.md) — 31% (state house)
- [WI House District 98](/us/states/wi/districts/house/98.md) — 25% (state house)
- [WI House District 22](/us/states/wi/districts/house/22.md) — 4% (state house)
- [WI House District 24](/us/states/wi/districts/house/24.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
