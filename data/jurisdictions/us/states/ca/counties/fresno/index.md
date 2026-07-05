---
type: Jurisdiction
title: "Fresno County, CA"
classification: county
fips: "06019"
state: "CA"
demographics:
  population: 1016725
  population_under_18: 282519
  population_18_64: 602718
  population_65_plus: 131488
  median_household_income: 74201
  poverty_rate: 18.31
  homeownership_rate: 55.55
  unemployment_rate: 8.69
  median_home_value: 388800
  gini_index: 0.4737
  vacancy_rate: 5.85
  race_white: 360596
  race_black: 44540
  race_asian: 114064
  race_native: 15039
  hispanic: 554390
  bachelors_plus: 208012
districts:
  - to: "us/states/ca/districts/13"
    rel: in-district
    area_weight: 0.4335
  - to: "us/states/ca/districts/05"
    rel: in-district
    area_weight: 0.3614
  - to: "us/states/ca/districts/20"
    rel: in-district
    area_weight: 0.1281
  - to: "us/states/ca/districts/21"
    rel: in-district
    area_weight: 0.076
  - to: "us/states/ca/districts/senate/14"
    rel: in-district
    area_weight: 0.5091
  - to: "us/states/ca/districts/senate/12"
    rel: in-district
    area_weight: 0.4851
  - to: "us/states/ca/districts/senate/16"
    rel: in-district
    area_weight: 0.0057
  - to: "us/states/ca/districts/house/8"
    rel: in-district
    area_weight: 0.484
  - to: "us/states/ca/districts/house/27"
    rel: in-district
    area_weight: 0.4121
  - to: "us/states/ca/districts/house/31"
    rel: in-district
    area_weight: 0.0961
  - to: "us/states/ca/districts/house/33"
    rel: in-district
    area_weight: 0.0078
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ca]
timestamp: "2026-07-03"
---

# Fresno County, CA

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1016725 |
| Under 18 | 282519 |
| 18–64 | 602718 |
| 65+ | 131488 |
| Median household income | 74201 |
| Poverty rate | 18.31 |
| Homeownership rate | 55.55 |
| Unemployment rate | 8.69 |
| Median home value | 388800 |
| Gini index | 0.4737 |
| Vacancy rate | 5.85 |
| White | 360596 |
| Black | 44540 |
| Asian | 114064 |
| Native | 15039 |
| Hispanic/Latino | 554390 |
| Bachelor's or higher | 208012 |

## Districts

- [CA-13](/us/states/ca/districts/13.md) — 43% (congressional)
- [CA-05](/us/states/ca/districts/05.md) — 36% (congressional)
- [CA-20](/us/states/ca/districts/20.md) — 13% (congressional)
- [CA-21](/us/states/ca/districts/21.md) — 8% (congressional)
- [CA Senate District 14](/us/states/ca/districts/senate/14.md) — 51% (state senate)
- [CA Senate District 12](/us/states/ca/districts/senate/12.md) — 49% (state senate)
- [CA Senate District 16](/us/states/ca/districts/senate/16.md) — 1% (state senate)
- [CA House District 8](/us/states/ca/districts/house/8.md) — 48% (state house)
- [CA House District 27](/us/states/ca/districts/house/27.md) — 41% (state house)
- [CA House District 31](/us/states/ca/districts/house/31.md) — 10% (state house)
- [CA House District 33](/us/states/ca/districts/house/33.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
