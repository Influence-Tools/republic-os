---
type: Jurisdiction
title: "Jefferson County, FL"
classification: county
fips: "12065"
state: "FL"
demographics:
  population: 15091
  population_under_18: 2589
  population_18_64: 8808
  population_65_plus: 3694
  median_household_income: 61212
  poverty_rate: 20.97
  homeownership_rate: 75.87
  unemployment_rate: 7.42
  median_home_value: 232600
  gini_index: 0.4515
  vacancy_rate: 16.48
  race_white: 9490
  race_black: 4197
  race_asian: 179
  race_native: 9
  hispanic: 765
  bachelors_plus: 3003
districts:
  - to: "us/states/fl/districts/02"
    rel: in-district
    area_weight: 0.9105
  - to: "us/states/fl/districts/senate/3"
    rel: in-district
    area_weight: 0.9113
  - to: "us/states/fl/districts/house/9"
    rel: in-district
    area_weight: 0.5584
  - to: "us/states/fl/districts/house/7"
    rel: in-district
    area_weight: 0.3528
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, fl]
timestamp: "2026-07-03"
---

# Jefferson County, FL

County jurisdiction — 21 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 15091 |
| Under 18 | 2589 |
| 18–64 | 8808 |
| 65+ | 3694 |
| Median household income | 61212 |
| Poverty rate | 20.97 |
| Homeownership rate | 75.87 |
| Unemployment rate | 7.42 |
| Median home value | 232600 |
| Gini index | 0.4515 |
| Vacancy rate | 16.48 |
| White | 9490 |
| Black | 4197 |
| Asian | 179 |
| Native | 9 |
| Hispanic/Latino | 765 |
| Bachelor's or higher | 3003 |

## Districts

- [FL-02](/us/states/fl/districts/02.md) — 91% (congressional)
- [FL Senate District 3](/us/states/fl/districts/senate/3.md) — 91% (state senate)
- [FL House District 9](/us/states/fl/districts/house/9.md) — 56% (state house)
- [FL House District 7](/us/states/fl/districts/house/7.md) — 35% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
