---
type: Jurisdiction
title: "Bedford County, VA"
classification: county
fips: "51019"
state: "VA"
demographics:
  population: 80894
  population_under_18: 15743
  population_18_64: 46331
  population_65_plus: 18820
  median_household_income: 78937
  poverty_rate: 8.06
  homeownership_rate: 84.66
  unemployment_rate: 3.07
  median_home_value: 297400
  gini_index: 0.4332
  vacancy_rate: 11.62
  race_white: 69252
  race_black: 5108
  race_asian: 1044
  race_native: 160
  hispanic: 2283
  bachelors_plus: 27797
districts:
  - to: "us/states/va/districts/09"
    rel: in-district
    area_weight: 0.8612
  - to: "us/states/va/districts/05"
    rel: in-district
    area_weight: 0.1351
  - to: "us/states/va/districts/senate/8"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/va/districts/house/51"
    rel: in-district
    area_weight: 0.5218
  - to: "us/states/va/districts/house/53"
    rel: in-district
    area_weight: 0.4778
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Bedford County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 80894 |
| Under 18 | 15743 |
| 18–64 | 46331 |
| 65+ | 18820 |
| Median household income | 78937 |
| Poverty rate | 8.06 |
| Homeownership rate | 84.66 |
| Unemployment rate | 3.07 |
| Median home value | 297400 |
| Gini index | 0.4332 |
| Vacancy rate | 11.62 |
| White | 69252 |
| Black | 5108 |
| Asian | 1044 |
| Native | 160 |
| Hispanic/Latino | 2283 |
| Bachelor's or higher | 27797 |

## Districts

- [VA-09](/us/states/va/districts/09.md) — 86% (congressional)
- [VA-05](/us/states/va/districts/05.md) — 14% (congressional)
- [VA Senate District 8](/us/states/va/districts/senate/8.md) — 100% (state senate)
- [VA House District 51](/us/states/va/districts/house/51.md) — 52% (state house)
- [VA House District 53](/us/states/va/districts/house/53.md) — 48% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
