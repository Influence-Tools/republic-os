---
type: Jurisdiction
title: "Henrico County, VA"
classification: county
fips: "51087"
state: "VA"
demographics:
  population: 335744
  population_under_18: 73554
  population_18_64: 205272
  population_65_plus: 56918
  median_household_income: 88783
  poverty_rate: 8.79
  homeownership_rate: 64.48
  unemployment_rate: 3.88
  median_home_value: 359200
  gini_index: 0.4713
  vacancy_rate: 5.21
  race_white: 169578
  race_black: 98584
  race_asian: 31613
  race_native: 745
  hispanic: 23193
  bachelors_plus: 155518
districts:
  - to: "us/states/va/districts/04"
    rel: in-district
    area_weight: 0.697
  - to: "us/states/va/districts/01"
    rel: in-district
    area_weight: 0.3018
  - to: "us/states/va/districts/senate/13"
    rel: in-district
    area_weight: 0.5566
  - to: "us/states/va/districts/senate/16"
    rel: in-district
    area_weight: 0.3479
  - to: "us/states/va/districts/senate/14"
    rel: in-district
    area_weight: 0.0943
  - to: "us/states/va/districts/house/81"
    rel: in-district
    area_weight: 0.5435
  - to: "us/states/va/districts/house/80"
    rel: in-district
    area_weight: 0.162
  - to: "us/states/va/districts/house/58"
    rel: in-district
    area_weight: 0.1319
  - to: "us/states/va/districts/house/57"
    rel: in-district
    area_weight: 0.1093
  - to: "us/states/va/districts/house/59"
    rel: in-district
    area_weight: 0.0526
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Henrico County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 335744 |
| Under 18 | 73554 |
| 18–64 | 205272 |
| 65+ | 56918 |
| Median household income | 88783 |
| Poverty rate | 8.79 |
| Homeownership rate | 64.48 |
| Unemployment rate | 3.88 |
| Median home value | 359200 |
| Gini index | 0.4713 |
| Vacancy rate | 5.21 |
| White | 169578 |
| Black | 98584 |
| Asian | 31613 |
| Native | 745 |
| Hispanic/Latino | 23193 |
| Bachelor's or higher | 155518 |

## Districts

- [VA-04](/us/states/va/districts/04.md) — 70% (congressional)
- [VA-01](/us/states/va/districts/01.md) — 30% (congressional)
- [VA Senate District 13](/us/states/va/districts/senate/13.md) — 56% (state senate)
- [VA Senate District 16](/us/states/va/districts/senate/16.md) — 35% (state senate)
- [VA Senate District 14](/us/states/va/districts/senate/14.md) — 9% (state senate)
- [VA House District 81](/us/states/va/districts/house/81.md) — 54% (state house)
- [VA House District 80](/us/states/va/districts/house/80.md) — 16% (state house)
- [VA House District 58](/us/states/va/districts/house/58.md) — 13% (state house)
- [VA House District 57](/us/states/va/districts/house/57.md) — 11% (state house)
- [VA House District 59](/us/states/va/districts/house/59.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
