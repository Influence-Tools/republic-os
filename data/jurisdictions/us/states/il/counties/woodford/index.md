---
type: Jurisdiction
title: "Woodford County, IL"
classification: county
fips: "17203"
state: "IL"
demographics:
  population: 38312
  population_under_18: 9161
  population_18_64: 21735
  population_65_plus: 7416
  median_household_income: 91483
  poverty_rate: 7.03
  homeownership_rate: 85.66
  unemployment_rate: 3.51
  median_home_value: 197600
  gini_index: 0.4104
  vacancy_rate: 6.81
  race_white: 36040
  race_black: 232
  race_asian: 229
  race_native: 65
  hispanic: 798
  bachelors_plus: 12682
districts:
  - to: "us/states/il/districts/16"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/senate/53"
    rel: in-district
    area_weight: 0.7076
  - to: "us/states/il/districts/senate/46"
    rel: in-district
    area_weight: 0.2187
  - to: "us/states/il/districts/senate/37"
    rel: in-district
    area_weight: 0.0604
  - to: "us/states/il/districts/senate/44"
    rel: in-district
    area_weight: 0.0134
  - to: "us/states/il/districts/house/105"
    rel: in-district
    area_weight: 0.7076
  - to: "us/states/il/districts/house/91"
    rel: in-district
    area_weight: 0.2186
  - to: "us/states/il/districts/house/73"
    rel: in-district
    area_weight: 0.0604
  - to: "us/states/il/districts/house/87"
    rel: in-district
    area_weight: 0.0134
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Woodford County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 38312 |
| Under 18 | 9161 |
| 18–64 | 21735 |
| 65+ | 7416 |
| Median household income | 91483 |
| Poverty rate | 7.03 |
| Homeownership rate | 85.66 |
| Unemployment rate | 3.51 |
| Median home value | 197600 |
| Gini index | 0.4104 |
| Vacancy rate | 6.81 |
| White | 36040 |
| Black | 232 |
| Asian | 229 |
| Native | 65 |
| Hispanic/Latino | 798 |
| Bachelor's or higher | 12682 |

## Districts

- [IL-16](/us/states/il/districts/16.md) — 100% (congressional)
- [IL Senate District 53](/us/states/il/districts/senate/53.md) — 71% (state senate)
- [IL Senate District 46](/us/states/il/districts/senate/46.md) — 22% (state senate)
- [IL Senate District 37](/us/states/il/districts/senate/37.md) — 6% (state senate)
- [IL Senate District 44](/us/states/il/districts/senate/44.md) — 1% (state senate)
- [IL House District 105](/us/states/il/districts/house/105.md) — 71% (state house)
- [IL House District 91](/us/states/il/districts/house/91.md) — 22% (state house)
- [IL House District 73](/us/states/il/districts/house/73.md) — 6% (state house)
- [IL House District 87](/us/states/il/districts/house/87.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
