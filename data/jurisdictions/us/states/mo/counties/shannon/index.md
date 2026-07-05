---
type: Jurisdiction
title: "Shannon County, MO"
classification: county
fips: "29203"
state: "MO"
demographics:
  population: 7177
  population_under_18: 1627
  population_18_64: 3934
  population_65_plus: 1616
  median_household_income: 55222
  poverty_rate: 18.03
  homeownership_rate: 79.94
  unemployment_rate: 1.3
  median_home_value: 157500
  gini_index: 0.4105
  vacancy_rate: 18.06
  race_white: 6622
  race_black: 14
  race_asian: 30
  race_native: 31
  hispanic: 48
  bachelors_plus: 890
districts:
  - to: "us/states/mo/districts/08"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/mo/districts/senate/33"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/mo/districts/house/144"
    rel: in-district
    area_weight: 0.7578
  - to: "us/states/mo/districts/house/153"
    rel: in-district
    area_weight: 0.2421
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mo]
timestamp: "2026-07-03"
---

# Shannon County, MO

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 7177 |
| Under 18 | 1627 |
| 18–64 | 3934 |
| 65+ | 1616 |
| Median household income | 55222 |
| Poverty rate | 18.03 |
| Homeownership rate | 79.94 |
| Unemployment rate | 1.3 |
| Median home value | 157500 |
| Gini index | 0.4105 |
| Vacancy rate | 18.06 |
| White | 6622 |
| Black | 14 |
| Asian | 30 |
| Native | 31 |
| Hispanic/Latino | 48 |
| Bachelor's or higher | 890 |

## Districts

- [MO-08](/us/states/mo/districts/08.md) — 100% (congressional)
- [MO Senate District 33](/us/states/mo/districts/senate/33.md) — 100% (state senate)
- [MO House District 144](/us/states/mo/districts/house/144.md) — 76% (state house)
- [MO House District 153](/us/states/mo/districts/house/153.md) — 24% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
