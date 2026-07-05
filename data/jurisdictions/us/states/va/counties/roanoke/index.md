---
type: Jurisdiction
title: "Roanoke County, VA"
classification: county
fips: "51161"
state: "VA"
demographics:
  population: 97023
  population_under_18: 19028
  population_18_64: 56527
  population_65_plus: 21468
  median_household_income: 83709
  poverty_rate: 7.26
  homeownership_rate: 75.69
  unemployment_rate: 2.75
  median_home_value: 286000
  gini_index: 0.4449
  vacancy_rate: 6.16
  race_white: 80836
  race_black: 6284
  race_asian: 3681
  race_native: 316
  hispanic: 3966
  bachelors_plus: 35462
districts:
  - to: "us/states/va/districts/06"
    rel: in-district
    area_weight: 0.652
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 0.348
  - to: "us/states/va/districts/senate/4"
    rel: in-district
    area_weight: 0.5038
  - to: "us/states/va/districts/senate/3"
    rel: in-district
    area_weight: 0.4958
  - to: "us/states/va/districts/house/41"
    rel: in-district
    area_weight: 0.6533
  - to: "us/states/va/districts/house/39"
    rel: in-district
    area_weight: 0.2111
  - to: "us/states/va/districts/house/40"
    rel: in-district
    area_weight: 0.1351
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Roanoke County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 97023 |
| Under 18 | 19028 |
| 18–64 | 56527 |
| 65+ | 21468 |
| Median household income | 83709 |
| Poverty rate | 7.26 |
| Homeownership rate | 75.69 |
| Unemployment rate | 2.75 |
| Median home value | 286000 |
| Gini index | 0.4449 |
| Vacancy rate | 6.16 |
| White | 80836 |
| Black | 6284 |
| Asian | 3681 |
| Native | 316 |
| Hispanic/Latino | 3966 |
| Bachelor's or higher | 35462 |

## Districts

- [VA-06](/us/states/va/districts/06.md) — 65% (congressional)
- [VA-09](/us/states/va/districts/09.md) — 35% (congressional)
- [VA Senate District 4](/us/states/va/districts/senate/4.md) — 50% (state senate)
- [VA Senate District 3](/us/states/va/districts/senate/3.md) — 50% (state senate)
- [VA House District 41](/us/states/va/districts/house/41.md) — 65% (state house)
- [VA House District 39](/us/states/va/districts/house/39.md) — 21% (state house)
- [VA House District 40](/us/states/va/districts/house/40.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
