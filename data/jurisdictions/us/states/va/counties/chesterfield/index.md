---
type: Jurisdiction
title: "Chesterfield County, VA"
classification: county
fips: "51041"
state: "VA"
demographics:
  population: 377869
  population_under_18: 89540
  population_18_64: 227498
  population_65_plus: 60831
  median_household_income: 101931
  poverty_rate: 7.06
  homeownership_rate: 76.73
  unemployment_rate: 4.64
  median_home_value: 366000
  gini_index: 0.4224
  vacancy_rate: 3.81
  race_white: 218762
  race_black: 88373
  race_asian: 13687
  race_native: 1276
  hispanic: 44796
  bachelors_plus: 155630
districts:
  - to: "us/states/va/districts/01"
    rel: in-district
    area_weight: 0.5107
  - to: "us/states/va/districts/04"
    rel: in-district
    area_weight: 0.4861
  - to: "us/states/va/districts/senate/12"
    rel: in-district
    area_weight: 0.7211
  - to: "us/states/va/districts/senate/15"
    rel: in-district
    area_weight: 0.2783
  - to: "us/states/va/districts/house/73"
    rel: in-district
    area_weight: 0.3552
  - to: "us/states/va/districts/house/74"
    rel: in-district
    area_weight: 0.3087
  - to: "us/states/va/districts/house/75"
    rel: in-district
    area_weight: 0.1278
  - to: "us/states/va/districts/house/76"
    rel: in-district
    area_weight: 0.0984
  - to: "us/states/va/districts/house/72"
    rel: in-district
    area_weight: 0.0434
  - to: "us/states/va/districts/house/77"
    rel: in-district
    area_weight: 0.0364
  - to: "us/states/va/districts/house/81"
    rel: in-district
    area_weight: 0.03
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Chesterfield County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 377869 |
| Under 18 | 89540 |
| 18–64 | 227498 |
| 65+ | 60831 |
| Median household income | 101931 |
| Poverty rate | 7.06 |
| Homeownership rate | 76.73 |
| Unemployment rate | 4.64 |
| Median home value | 366000 |
| Gini index | 0.4224 |
| Vacancy rate | 3.81 |
| White | 218762 |
| Black | 88373 |
| Asian | 13687 |
| Native | 1276 |
| Hispanic/Latino | 44796 |
| Bachelor's or higher | 155630 |

## Districts

- [VA-01](/us/states/va/districts/01.md) — 51% (congressional)
- [VA-04](/us/states/va/districts/04.md) — 49% (congressional)
- [VA Senate District 12](/us/states/va/districts/senate/12.md) — 72% (state senate)
- [VA Senate District 15](/us/states/va/districts/senate/15.md) — 28% (state senate)
- [VA House District 73](/us/states/va/districts/house/73.md) — 36% (state house)
- [VA House District 74](/us/states/va/districts/house/74.md) — 31% (state house)
- [VA House District 75](/us/states/va/districts/house/75.md) — 13% (state house)
- [VA House District 76](/us/states/va/districts/house/76.md) — 10% (state house)
- [VA House District 72](/us/states/va/districts/house/72.md) — 4% (state house)
- [VA House District 77](/us/states/va/districts/house/77.md) — 4% (state house)
- [VA House District 81](/us/states/va/districts/house/81.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
