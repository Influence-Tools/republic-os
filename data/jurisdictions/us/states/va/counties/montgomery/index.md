---
type: Jurisdiction
title: "Montgomery County, VA"
classification: county
fips: "51121"
state: "VA"
demographics:
  population: 99101
  population_under_18: 15115
  population_18_64: 70028
  population_65_plus: 13958
  median_household_income: 72715
  poverty_rate: 23.95
  homeownership_rate: 55.3
  unemployment_rate: 2.93
  median_home_value: 304600
  gini_index: 0.5104
  vacancy_rate: 13.63
  race_white: 81034
  race_black: 3878
  race_asian: 6434
  race_native: 189
  hispanic: 4602
  bachelors_plus: 42057
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/va/districts/senate/4"
    rel: in-district
    area_weight: 0.5908
  - to: "us/states/va/districts/senate/5"
    rel: in-district
    area_weight: 0.409
  - to: "us/states/va/districts/house/41"
    rel: in-district
    area_weight: 0.8392
  - to: "us/states/va/districts/house/42"
    rel: in-district
    area_weight: 0.1606
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Montgomery County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 99101 |
| Under 18 | 15115 |
| 18–64 | 70028 |
| 65+ | 13958 |
| Median household income | 72715 |
| Poverty rate | 23.95 |
| Homeownership rate | 55.3 |
| Unemployment rate | 2.93 |
| Median home value | 304600 |
| Gini index | 0.5104 |
| Vacancy rate | 13.63 |
| White | 81034 |
| Black | 3878 |
| Asian | 6434 |
| Native | 189 |
| Hispanic/Latino | 4602 |
| Bachelor's or higher | 42057 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 100% (congressional)
- [VA Senate District 4](/us/states/va/districts/senate/4.md) — 59% (state senate)
- [VA Senate District 5](/us/states/va/districts/senate/5.md) — 41% (state senate)
- [VA House District 41](/us/states/va/districts/house/41.md) — 84% (state house)
- [VA House District 42](/us/states/va/districts/house/42.md) — 16% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
