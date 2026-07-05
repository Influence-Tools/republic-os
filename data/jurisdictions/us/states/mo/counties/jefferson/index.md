---
type: Jurisdiction
title: "Jefferson County, MO"
classification: county
fips: "29099"
state: "MO"
demographics:
  population: 229458
  population_under_18: 51633
  population_18_64: 139564
  population_65_plus: 38261
  median_household_income: 82851
  poverty_rate: 9.03
  homeownership_rate: 82.23
  unemployment_rate: 3.2
  median_home_value: 237200
  gini_index: 0.395
  vacancy_rate: 6.01
  race_white: 204876
  race_black: 2315
  race_asian: 2358
  race_native: 351
  hispanic: 6066
  bachelors_plus: 52596
districts:
  - to: "us/states/mo/districts/03"
    rel: in-district
    area_weight: 0.5034
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 0.4945
  - to: "us/states/mo/districts/senate/3"
    rel: in-district
    area_weight: 0.5211
  - to: "us/states/mo/districts/senate/22"
    rel: in-district
    area_weight: 0.4782
  - to: "us/states/mo/districts/house/115"
    rel: in-district
    area_weight: 0.4801
  - to: "us/states/mo/districts/house/111"
    rel: in-district
    area_weight: 0.2348
  - to: "us/states/mo/districts/house/112"
    rel: in-district
    area_weight: 0.0817
  - to: "us/states/mo/districts/house/97"
    rel: in-district
    area_weight: 0.0496
  - to: "us/states/mo/districts/house/113"
    rel: in-district
    area_weight: 0.0405
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Jefferson County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 229458 |
| Under 18 | 51633 |
| 18–64 | 139564 |
| 65+ | 38261 |
| Median household income | 82851 |
| Poverty rate | 9.03 |
| Homeownership rate | 82.23 |
| Unemployment rate | 3.2 |
| Median home value | 237200 |
| Gini index | 0.395 |
| Vacancy rate | 6.01 |
| White | 204876 |
| Black | 2315 |
| Asian | 2358 |
| Native | 351 |
| Hispanic/Latino | 6066 |
| Bachelor's or higher | 52596 |

## Districts

- [MO-03](/us/states/mo/districts/03.md) — 50% (congressional)
- [MO-08](/us/states/mo/districts/08.md) — 49% (congressional)
- [MO Senate District 3](/us/states/mo/districts/senate/3.md) — 52% (state senate)
- [MO Senate District 22](/us/states/mo/districts/senate/22.md) — 48% (state senate)
- [MO House District 115](/us/states/mo/districts/house/115.md) — 48% (state house)
- [MO House District 111](/us/states/mo/districts/house/111.md) — 23% (state house)
- [MO House District 112](/us/states/mo/districts/house/112.md) — 8% (state house)
- [MO House District 97](/us/states/mo/districts/house/97.md) — 5% (state house)
- [MO House District 113](/us/states/mo/districts/house/113.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
