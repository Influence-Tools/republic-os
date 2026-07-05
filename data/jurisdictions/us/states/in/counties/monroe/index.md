---
type: Jurisdiction
title: "Monroe County, IN"
classification: county
fips: "18105"
state: "IN"
demographics:
  population: 140965
  population_under_18: 22129
  population_18_64: 98189
  population_65_plus: 20647
  median_household_income: 65868
  poverty_rate: 19.68
  homeownership_rate: 53.97
  unemployment_rate: 5.51
  median_home_value: 285200
  gini_index: 0.4988
  vacancy_rate: 9.78
  race_white: 115589
  race_black: 4988
  race_asian: 9644
  race_native: 219
  hispanic: 6736
  bachelors_plus: 62538
districts:
  - to: "us/states/in/districts/09"
    rel: in-district
    area_weight: 0.9991
  - to: "us/states/in/districts/senate/40"
    rel: in-district
    area_weight: 0.7193
  - to: "us/states/in/districts/senate/44"
    rel: in-district
    area_weight: 0.2806
  - to: "us/states/in/districts/house/62"
    rel: in-district
    area_weight: 0.6077
  - to: "us/states/in/districts/house/46"
    rel: in-district
    area_weight: 0.1748
  - to: "us/states/in/districts/house/60"
    rel: in-district
    area_weight: 0.1682
  - to: "us/states/in/districts/house/61"
    rel: in-district
    area_weight: 0.0493
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, in]
timestamp: "2026-07-03"
---

# Monroe County, IN

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 140965 |
| Under 18 | 22129 |
| 18–64 | 98189 |
| 65+ | 20647 |
| Median household income | 65868 |
| Poverty rate | 19.68 |
| Homeownership rate | 53.97 |
| Unemployment rate | 5.51 |
| Median home value | 285200 |
| Gini index | 0.4988 |
| Vacancy rate | 9.78 |
| White | 115589 |
| Black | 4988 |
| Asian | 9644 |
| Native | 219 |
| Hispanic/Latino | 6736 |
| Bachelor's or higher | 62538 |

## Districts

- [IN-09](/us/states/in/districts/09.md) — 100% (congressional)
- [IN Senate District 40](/us/states/in/districts/senate/40.md) — 72% (state senate)
- [IN Senate District 44](/us/states/in/districts/senate/44.md) — 28% (state senate)
- [IN House District 62](/us/states/in/districts/house/62.md) — 61% (state house)
- [IN House District 46](/us/states/in/districts/house/46.md) — 17% (state house)
- [IN House District 60](/us/states/in/districts/house/60.md) — 17% (state house)
- [IN House District 61](/us/states/in/districts/house/61.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
