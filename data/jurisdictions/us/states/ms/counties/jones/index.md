---
type: Jurisdiction
title: "Jones County, MS"
classification: county
fips: "28067"
state: "MS"
demographics:
  population: 66472
  population_under_18: 16685
  population_18_64: 37936
  population_65_plus: 11851
  median_household_income: 52216
  poverty_rate: 18.74
  homeownership_rate: 75.1
  unemployment_rate: 4.0
  median_home_value: 143100
  gini_index: 0.4855
  vacancy_rate: 13.42
  race_white: 42657
  race_black: 18974
  race_asian: 256
  race_native: 462
  hispanic: 4177
  bachelors_plus: 12512
districts:
  - to: "us/states/ms/districts/04"
    rel: in-district
    area_weight: 0.9003
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 0.0997
  - to: "us/states/ms/districts/senate/42"
    rel: in-district
    area_weight: 0.7237
  - to: "us/states/ms/districts/senate/34"
    rel: in-district
    area_weight: 0.2762
  - to: "us/states/ms/districts/house/88"
    rel: in-district
    area_weight: 0.6337
  - to: "us/states/ms/districts/house/89"
    rel: in-district
    area_weight: 0.2153
  - to: "us/states/ms/districts/house/80"
    rel: in-district
    area_weight: 0.0762
  - to: "us/states/ms/districts/house/90"
    rel: in-district
    area_weight: 0.0748
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Jones County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 66472 |
| Under 18 | 16685 |
| 18–64 | 37936 |
| 65+ | 11851 |
| Median household income | 52216 |
| Poverty rate | 18.74 |
| Homeownership rate | 75.1 |
| Unemployment rate | 4.0 |
| Median home value | 143100 |
| Gini index | 0.4855 |
| Vacancy rate | 13.42 |
| White | 42657 |
| Black | 18974 |
| Asian | 256 |
| Native | 462 |
| Hispanic/Latino | 4177 |
| Bachelor's or higher | 12512 |

## Districts

- [MS-04](/us/states/ms/districts/04.md) — 90% (congressional)
- [MS-03](/us/states/ms/districts/03.md) — 10% (congressional)
- [MS Senate District 42](/us/states/ms/districts/senate/42.md) — 72% (state senate)
- [MS Senate District 34](/us/states/ms/districts/senate/34.md) — 28% (state senate)
- [MS House District 88](/us/states/ms/districts/house/88.md) — 63% (state house)
- [MS House District 89](/us/states/ms/districts/house/89.md) — 22% (state house)
- [MS House District 80](/us/states/ms/districts/house/80.md) — 8% (state house)
- [MS House District 90](/us/states/ms/districts/house/90.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
