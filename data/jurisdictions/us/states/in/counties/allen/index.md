---
type: Jurisdiction
title: "Allen County, IN"
classification: county
fips: "18003"
state: "IN"
demographics:
  population: 392378
  population_under_18: 99630
  population_18_64: 231470
  population_65_plus: 61278
  median_household_income: 70737
  poverty_rate: 12.51
  homeownership_rate: 68.87
  unemployment_rate: 4.69
  median_home_value: 214900
  gini_index: 0.4491
  vacancy_rate: 5.84
  race_white: 279390
  race_black: 41585
  race_asian: 20833
  race_native: 2233
  hispanic: 35389
  bachelors_plus: 108333
districts:
  - to: "us/states/in/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/in/districts/senate/14"
    rel: in-district
    area_weight: 0.5277
  - to: "us/states/in/districts/senate/16"
    rel: in-district
    area_weight: 0.2167
  - to: "us/states/in/districts/senate/19"
    rel: in-district
    area_weight: 0.1329
  - to: "us/states/in/districts/senate/15"
    rel: in-district
    area_weight: 0.1227
  - to: "us/states/in/districts/house/85"
    rel: in-district
    area_weight: 0.6146
  - to: "us/states/in/districts/house/81"
    rel: in-district
    area_weight: 0.1988
  - to: "us/states/in/districts/house/83"
    rel: in-district
    area_weight: 0.0595
  - to: "us/states/in/districts/house/84"
    rel: in-district
    area_weight: 0.0494
  - to: "us/states/in/districts/house/80"
    rel: in-district
    area_weight: 0.0397
  - to: "us/states/in/districts/house/82"
    rel: in-district
    area_weight: 0.0375
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Allen County, IN

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 392378 |
| Under 18 | 99630 |
| 18–64 | 231470 |
| 65+ | 61278 |
| Median household income | 70737 |
| Poverty rate | 12.51 |
| Homeownership rate | 68.87 |
| Unemployment rate | 4.69 |
| Median home value | 214900 |
| Gini index | 0.4491 |
| Vacancy rate | 5.84 |
| White | 279390 |
| Black | 41585 |
| Asian | 20833 |
| Native | 2233 |
| Hispanic/Latino | 35389 |
| Bachelor's or higher | 108333 |

## Districts

- [IN-03](/us/states/in/districts/03.md) — 100% (congressional)
- [IN Senate District 14](/us/states/in/districts/senate/14.md) — 53% (state senate)
- [IN Senate District 16](/us/states/in/districts/senate/16.md) — 22% (state senate)
- [IN Senate District 19](/us/states/in/districts/senate/19.md) — 13% (state senate)
- [IN Senate District 15](/us/states/in/districts/senate/15.md) — 12% (state senate)
- [IN House District 85](/us/states/in/districts/house/85.md) — 61% (state house)
- [IN House District 81](/us/states/in/districts/house/81.md) — 20% (state house)
- [IN House District 83](/us/states/in/districts/house/83.md) — 6% (state house)
- [IN House District 84](/us/states/in/districts/house/84.md) — 5% (state house)
- [IN House District 80](/us/states/in/districts/house/80.md) — 4% (state house)
- [IN House District 82](/us/states/in/districts/house/82.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
