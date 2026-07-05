---
type: Jurisdiction
title: "Champaign County, IL"
classification: county
fips: "17019"
state: "IL"
demographics:
  population: 208741
  population_under_18: 39863
  population_18_64: 139894
  population_65_plus: 28984
  median_household_income: 63683
  poverty_rate: 19.07
  homeownership_rate: 54.02
  unemployment_rate: 4.3
  median_home_value: 211500
  gini_index: 0.5147
  vacancy_rate: 10.14
  race_white: 134024
  race_black: 28079
  race_asian: 23898
  race_native: 381
  hispanic: 17249
  bachelors_plus: 86606
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.6216
  - to: "us/states/il/districts/13"
    rel: in-district
    area_weight: 0.1924
  - to: "us/states/il/districts/02"
    rel: in-district
    area_weight: 0.1859
  - to: "us/states/il/districts/senate/51"
    rel: in-district
    area_weight: 0.684
  - to: "us/states/il/districts/senate/52"
    rel: in-district
    area_weight: 0.3159
  - to: "us/states/il/districts/house/101"
    rel: in-district
    area_weight: 0.586
  - to: "us/states/il/districts/house/104"
    rel: in-district
    area_weight: 0.2901
  - to: "us/states/il/districts/house/102"
    rel: in-district
    area_weight: 0.0981
  - to: "us/states/il/districts/house/103"
    rel: in-district
    area_weight: 0.0258
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Champaign County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 208741 |
| Under 18 | 39863 |
| 18–64 | 139894 |
| 65+ | 28984 |
| Median household income | 63683 |
| Poverty rate | 19.07 |
| Homeownership rate | 54.02 |
| Unemployment rate | 4.3 |
| Median home value | 211500 |
| Gini index | 0.5147 |
| Vacancy rate | 10.14 |
| White | 134024 |
| Black | 28079 |
| Asian | 23898 |
| Native | 381 |
| Hispanic/Latino | 17249 |
| Bachelor's or higher | 86606 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 62% (congressional)
- [IL-13](/us/states/il/districts/13.md) — 19% (congressional)
- [IL-02](/us/states/il/districts/02.md) — 19% (congressional)
- [IL Senate District 51](/us/states/il/districts/senate/51.md) — 68% (state senate)
- [IL Senate District 52](/us/states/il/districts/senate/52.md) — 32% (state senate)
- [IL House District 101](/us/states/il/districts/house/101.md) — 59% (state house)
- [IL House District 104](/us/states/il/districts/house/104.md) — 29% (state house)
- [IL House District 102](/us/states/il/districts/house/102.md) — 10% (state house)
- [IL House District 103](/us/states/il/districts/house/103.md) — 3% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
