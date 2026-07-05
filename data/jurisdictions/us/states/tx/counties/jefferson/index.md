---
type: Jurisdiction
title: "Jefferson County, TX"
classification: county
fips: "48245"
state: "TX"
demographics:
  population: 253878
  population_under_18: 62480
  population_18_64: 152135
  population_65_plus: 39263
  median_household_income: 60026
  poverty_rate: 19.49
  homeownership_rate: 62.5
  unemployment_rate: 6.31
  median_home_value: 169500
  gini_index: 0.4768
  vacancy_rate: 13.72
  race_white: 101964
  race_black: 83680
  race_asian: 9630
  race_native: 1566
  hispanic: 61240
  bachelors_plus: 44212
districts:
  - to: "us/states/tx/districts/14"
    rel: in-district
    area_weight: 0.6542
  - to: "us/states/tx/districts/36"
    rel: in-district
    area_weight: 0.2322
  - to: "us/states/tx/districts/senate/4"
    rel: in-district
    area_weight: 0.7334
  - to: "us/states/tx/districts/senate/3"
    rel: in-district
    area_weight: 0.1527
  - to: "us/states/tx/districts/house/21"
    rel: in-district
    area_weight: 0.6769
  - to: "us/states/tx/districts/house/22"
    rel: in-district
    area_weight: 0.2089
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Jefferson County, TX

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 253878 |
| Under 18 | 62480 |
| 18–64 | 152135 |
| 65+ | 39263 |
| Median household income | 60026 |
| Poverty rate | 19.49 |
| Homeownership rate | 62.5 |
| Unemployment rate | 6.31 |
| Median home value | 169500 |
| Gini index | 0.4768 |
| Vacancy rate | 13.72 |
| White | 101964 |
| Black | 83680 |
| Asian | 9630 |
| Native | 1566 |
| Hispanic/Latino | 61240 |
| Bachelor's or higher | 44212 |

## Districts

- [TX-14](/us/states/tx/districts/14.md) — 65% (congressional)
- [TX-36](/us/states/tx/districts/36.md) — 23% (congressional)
- [TX Senate District 4](/us/states/tx/districts/senate/4.md) — 73% (state senate)
- [TX Senate District 3](/us/states/tx/districts/senate/3.md) — 15% (state senate)
- [TX House District 21](/us/states/tx/districts/house/21.md) — 68% (state house)
- [TX House District 22](/us/states/tx/districts/house/22.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
