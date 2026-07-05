---
type: Jurisdiction
title: "Norfolk city, VA"
classification: county
fips: "51710"
state: "VA"
demographics:
  population: 233596
  population_under_18: 55904
  population_18_64: 99700
  population_65_plus: 77992
  median_household_income: 66109
  poverty_rate: 16.5
  homeownership_rate: 46.33
  unemployment_rate: 5.7
  median_home_value: 289900
  gini_index: 0.4736
  vacancy_rate: 8.27
  race_white: 100966
  race_black: 92432
  race_asian: 8544
  race_native: 1544
  hispanic: 23691
  bachelors_plus: 72093
districts:
  - to: "us/states/va/districts/03"
    rel: in-district
    area_weight: 0.6387
  - to: "us/states/va/districts/02"
    rel: in-district
    area_weight: 0.0051
  - to: "us/states/va/districts/senate/21"
    rel: in-district
    area_weight: 0.5692
  - to: "us/states/va/districts/senate/20"
    rel: in-district
    area_weight: 0.0507
  - to: "us/states/va/districts/house/94"
    rel: in-district
    area_weight: 0.2222
  - to: "us/states/va/districts/house/93"
    rel: in-district
    area_weight: 0.2187
  - to: "us/states/va/districts/house/92"
    rel: in-district
    area_weight: 0.1351
  - to: "us/states/va/districts/house/95"
    rel: in-district
    area_weight: 0.044
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Norfolk city, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 233596 |
| Under 18 | 55904 |
| 18–64 | 99700 |
| 65+ | 77992 |
| Median household income | 66109 |
| Poverty rate | 16.5 |
| Homeownership rate | 46.33 |
| Unemployment rate | 5.7 |
| Median home value | 289900 |
| Gini index | 0.4736 |
| Vacancy rate | 8.27 |
| White | 100966 |
| Black | 92432 |
| Asian | 8544 |
| Native | 1544 |
| Hispanic/Latino | 23691 |
| Bachelor's or higher | 72093 |

## Districts

- [VA-03](/us/states/va/districts/03.md) — 64% (congressional)
- [VA-02](/us/states/va/districts/02.md) — 1% (congressional)
- [VA Senate District 21](/us/states/va/districts/senate/21.md) — 57% (state senate)
- [VA Senate District 20](/us/states/va/districts/senate/20.md) — 5% (state senate)
- [VA House District 94](/us/states/va/districts/house/94.md) — 22% (state house)
- [VA House District 93](/us/states/va/districts/house/93.md) — 22% (state house)
- [VA House District 92](/us/states/va/districts/house/92.md) — 14% (state house)
- [VA House District 95](/us/states/va/districts/house/95.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
