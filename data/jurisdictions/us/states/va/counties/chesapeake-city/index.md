---
type: Jurisdiction
title: "Chesapeake city, VA"
classification: county
fips: "51550"
state: "VA"
demographics:
  population: 254997
  population_under_18: 69377
  population_18_64: 84222
  population_65_plus: 101398
  median_household_income: 89265
  poverty_rate: 11.79
  homeownership_rate: 72.21
  unemployment_rate: 4.64
  median_home_value: 388600
  gini_index: 0.4279
  vacancy_rate: 2.94
  race_white: 138007
  race_black: 75527
  race_asian: 11300
  race_native: 557
  hispanic: 20969
  bachelors_plus: 82424
districts:
  - to: "us/states/va/districts/02"
    rel: in-district
    area_weight: 0.8618
  - to: "us/states/va/districts/03"
    rel: in-district
    area_weight: 0.1377
  - to: "us/states/va/districts/senate/19"
    rel: in-district
    area_weight: 0.8053
  - to: "us/states/va/districts/senate/18"
    rel: in-district
    area_weight: 0.1938
  - to: "us/states/va/districts/house/90"
    rel: in-district
    area_weight: 0.5319
  - to: "us/states/va/districts/house/89"
    rel: in-district
    area_weight: 0.3475
  - to: "us/states/va/districts/house/91"
    rel: in-district
    area_weight: 0.1033
  - to: "us/states/va/districts/house/92"
    rel: in-district
    area_weight: 0.0169
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Chesapeake city, VA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 254997 |
| Under 18 | 69377 |
| 18–64 | 84222 |
| 65+ | 101398 |
| Median household income | 89265 |
| Poverty rate | 11.79 |
| Homeownership rate | 72.21 |
| Unemployment rate | 4.64 |
| Median home value | 388600 |
| Gini index | 0.4279 |
| Vacancy rate | 2.94 |
| White | 138007 |
| Black | 75527 |
| Asian | 11300 |
| Native | 557 |
| Hispanic/Latino | 20969 |
| Bachelor's or higher | 82424 |

## Districts

- [VA-02](/us/states/va/districts/02.md) — 86% (congressional)
- [VA-03](/us/states/va/districts/03.md) — 14% (congressional)
- [VA Senate District 19](/us/states/va/districts/senate/19.md) — 81% (state senate)
- [VA Senate District 18](/us/states/va/districts/senate/18.md) — 19% (state senate)
- [VA House District 90](/us/states/va/districts/house/90.md) — 53% (state house)
- [VA House District 89](/us/states/va/districts/house/89.md) — 35% (state house)
- [VA House District 91](/us/states/va/districts/house/91.md) — 10% (state house)
- [VA House District 92](/us/states/va/districts/house/92.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
