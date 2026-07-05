---
type: Jurisdiction
title: "Tippecanoe County, IN"
classification: county
fips: "18157"
state: "IN"
demographics:
  population: 189071
  population_under_18: 38352
  population_18_64: 127496
  population_65_plus: 23223
  median_household_income: 60636
  poverty_rate: 19.21
  homeownership_rate: 53.38
  unemployment_rate: 3.25
  median_home_value: 239300
  gini_index: 0.4779
  vacancy_rate: 6.0
  race_white: 140140
  race_black: 11832
  race_asian: 15233
  race_native: 228
  hispanic: 19548
  bachelors_plus: 61258
districts:
  - to: "us/states/in/districts/04"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/in/districts/senate/22"
    rel: in-district
    area_weight: 0.5299
  - to: "us/states/in/districts/senate/23"
    rel: in-district
    area_weight: 0.4699
  - to: "us/states/in/districts/house/13"
    rel: in-district
    area_weight: 0.4518
  - to: "us/states/in/districts/house/41"
    rel: in-district
    area_weight: 0.2513
  - to: "us/states/in/districts/house/26"
    rel: in-district
    area_weight: 0.1181
  - to: "us/states/in/districts/house/38"
    rel: in-district
    area_weight: 0.1103
  - to: "us/states/in/districts/house/27"
    rel: in-district
    area_weight: 0.0683
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Tippecanoe County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 189071 |
| Under 18 | 38352 |
| 18–64 | 127496 |
| 65+ | 23223 |
| Median household income | 60636 |
| Poverty rate | 19.21 |
| Homeownership rate | 53.38 |
| Unemployment rate | 3.25 |
| Median home value | 239300 |
| Gini index | 0.4779 |
| Vacancy rate | 6.0 |
| White | 140140 |
| Black | 11832 |
| Asian | 15233 |
| Native | 228 |
| Hispanic/Latino | 19548 |
| Bachelor's or higher | 61258 |

## Districts

- [IN-04](/us/states/in/districts/04.md) — 100% (congressional)
- [IN Senate District 22](/us/states/in/districts/senate/22.md) — 53% (state senate)
- [IN Senate District 23](/us/states/in/districts/senate/23.md) — 47% (state senate)
- [IN House District 13](/us/states/in/districts/house/13.md) — 45% (state house)
- [IN House District 41](/us/states/in/districts/house/41.md) — 25% (state house)
- [IN House District 26](/us/states/in/districts/house/26.md) — 12% (state house)
- [IN House District 38](/us/states/in/districts/house/38.md) — 11% (state house)
- [IN House District 27](/us/states/in/districts/house/27.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
