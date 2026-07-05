---
type: Jurisdiction
title: "Monroe County, MS"
classification: county
fips: "28095"
state: "MS"
demographics:
  population: 33747
  population_under_18: 7551
  population_18_64: 19303
  population_65_plus: 6893
  median_household_income: 51866
  poverty_rate: 18.04
  homeownership_rate: 76.32
  unemployment_rate: 6.31
  median_home_value: 120800
  gini_index: 0.4577
  vacancy_rate: 17.5
  race_white: 22638
  race_black: 10034
  race_asian: 107
  race_native: 89
  hispanic: 535
  bachelors_plus: 5010
districts:
  - to: "us/states/ms/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/senate/7"
    rel: in-district
    area_weight: 0.6661
  - to: "us/states/ms/districts/senate/17"
    rel: in-district
    area_weight: 0.3336
  - to: "us/states/ms/districts/house/39"
    rel: in-district
    area_weight: 0.2505
  - to: "us/states/ms/districts/house/36"
    rel: in-district
    area_weight: 0.2298
  - to: "us/states/ms/districts/house/22"
    rel: in-district
    area_weight: 0.1753
  - to: "us/states/ms/districts/house/21"
    rel: in-district
    area_weight: 0.1563
  - to: "us/states/ms/districts/house/37"
    rel: in-district
    area_weight: 0.1331
  - to: "us/states/ms/districts/house/16"
    rel: in-district
    area_weight: 0.0548
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Monroe County, MS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 33747 |
| Under 18 | 7551 |
| 18–64 | 19303 |
| 65+ | 6893 |
| Median household income | 51866 |
| Poverty rate | 18.04 |
| Homeownership rate | 76.32 |
| Unemployment rate | 6.31 |
| Median home value | 120800 |
| Gini index | 0.4577 |
| Vacancy rate | 17.5 |
| White | 22638 |
| Black | 10034 |
| Asian | 107 |
| Native | 89 |
| Hispanic/Latino | 535 |
| Bachelor's or higher | 5010 |

## Districts

- [MS-01](/us/states/ms/districts/01.md) — 100% (congressional)
- [MS Senate District 7](/us/states/ms/districts/senate/7.md) — 67% (state senate)
- [MS Senate District 17](/us/states/ms/districts/senate/17.md) — 33% (state senate)
- [MS House District 39](/us/states/ms/districts/house/39.md) — 25% (state house)
- [MS House District 36](/us/states/ms/districts/house/36.md) — 23% (state house)
- [MS House District 22](/us/states/ms/districts/house/22.md) — 18% (state house)
- [MS House District 21](/us/states/ms/districts/house/21.md) — 16% (state house)
- [MS House District 37](/us/states/ms/districts/house/37.md) — 13% (state house)
- [MS House District 16](/us/states/ms/districts/house/16.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
